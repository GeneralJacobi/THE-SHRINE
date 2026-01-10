## this is Vibe Coded nonsense but it works quite well
# i dont claim to have  written this
# but i hope it helps #LOL


import sys

# --- ANSI Color Codes ---
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'    # Opcode
    GREEN = '\033[92m'   # Source / Ad Mode
    YELLOW = '\033[93m'  # Byte/Word or Condition
    MAGENTA = '\033[95m' # Destination / Register
    RED = '\033[91m'
    GREY = '\033[90m'    # Prefix / Inactive
    ORANGE = '\033[38;5;208m' # Extension / Offset
    BOLD = '\033[1m'
    RESET = '\033[0m'

# --- Lookup Tables ---
single_opcode_map = {
    0b000: 'rrc', 0b001: 'swpb', 0b010: 'rra', 0b011: 'sxt',
    0b100: 'push', 0b101: 'call', 0b110: 'reti'
}

jump_opcode_map = {
    0b000: 'jne', 0b001: 'jeq', 0b010: 'jnc', 0b011: 'jc',
    0b100: 'jn',  0b101: 'jge', 0b110: 'jl',  0b111: 'jmp'
}

double_opcode_map = {
    0x4: 'mov', 0x5: 'add', 0x6: 'addc', 0x7: 'subc',
    0x8: 'sub', 0x9: 'cmp', 0xA: 'dadd', 0xB: 'bit',
    0xC: 'bic', 0xD: 'bis', 0xE: 'xor', 0xF: 'and'
}

bw_mode = { 0: 'word', 1: 'byte' }

# --- Helper Functions for Formatting ---
def format_source_operand(reg, as_mode, extension=None, bw=0):
    """
    Decodes Source Operand based on Register and As Mode.
    Handles R0(PC), R2(SR/CG1), R3(CG2) special cases.
    """
    # 1. Constant Generator (R3) & SR (R2)
    if reg == 3: # CG2
        val = {0: '#0', 1: '#1', 2: '#2', 3: '#-1'}[as_mode]
        return val, "constant"
    if reg == 2: # SR / CG1
        if as_mode == 2: return '#4', "constant"
        if as_mode == 3: return '#8', "constant"

    # 2. General Addressing
    if as_mode == 0b00: # Register Direct
        return f"r{reg}", "register direct"
    
    elif as_mode == 0b01: # Indexed (X(Rn)) or Symbolic (Addr if R0)
        ext_str = f"0x{extension:04x}" if extension is not None else "X"
        desc = "indexed"
        
        if reg == 0: # PC Relative (Symbolic)
            return f"{ext_str}(pc)", "symbolic (pc rel)"
        if reg == 2: # Absolute Address &ADDR
            return f"&{ext_str}", "absolute"
        
        return f"{ext_str}(r{reg})", desc

    elif as_mode == 0b10: # Register Indirect
        return f"@r{reg}", "register indirect"
    
    elif as_mode == 0b11: # Indirect Autoincrement or Immediate
        if reg == 0: # PC -> Immediate
            val = f"#{extension}" if extension is not None else "#IMM"
            if extension is not None and extension > 9:
                val += f" (0x{extension:04x})"
            return val, "immediate"
        return f"@r{reg}+", "indirect auto-inc"

    return "??", "??"

def format_dest_operand(reg, ad_mode, extension=None):
    """
    Decodes Destination Operand based on Register and Ad Mode.
    """
    if ad_mode == 0:
        return f"r{reg}", "register direct"
    else: # ad_mode == 1 (Indexed)
        ext_str = f"0x{extension:04x}" if extension is not None else "X"
        if reg == 0: return f"{ext_str}(pc)", "symbolic"
        if reg == 2: return f"&{ext_str}", "absolute"
        return f"{ext_str}(r{reg})", "indexed"

# --- Base Class ---
class InstructionBase:
    def __init__(self, opcode: int, extension: int = None):
        self.opcode = opcode & 0xFFFF
        self.extension = extension
        self.core = bin(self.opcode)[2:].zfill(16)
        self.parse()

    def yoink(self, start, end, color_code):
        val = self.core[start:end]
        return (f"{Colors.GREY}{'.' * start}{Colors.RESET}"
                f"{color_code}{val}{Colors.RESET}"
                f"{Colors.GREY}{'.' * (16-end)}{Colors.RESET}")
    
    def parse(self):
        raise NotImplementedError

# --- Format I: Double Operand ---
class DoubleOp(InstructionBase):
    ''' 
    15-12 | 11-8  | 7  | 6   | 5-4 | 3-0
    Op    | S-Reg | Ad | B/W | As  | D-Reg
    '''
    def parse(self):
        self.op_bits = (self.opcode >> 12) & 0xF
        self.src_reg = (self.opcode >> 8) & 0xF
        self.ad_bit  = (self.opcode >> 7) & 0x1
        self.bw_bit  = (self.opcode >> 6) & 0x1
        self.as_bits = (self.opcode >> 4) & 0x3
        self.dst_reg = self.opcode & 0xF

        self.name = double_opcode_map.get(self.op_bits, "invalid")
        self.suffix = '.b' if self.bw_bit else '.w'
        
        # Smart Formatting
        self.src_str, self.src_desc = format_source_operand(self.src_reg, self.as_bits, self.extension, self.bw_bit)
        
        # Note: If Src used the extension word, Dst cannot use it in this simple parser 
        # (MSP430 supports 2 extension words, handling that requires a stream parser).
        # We assume if Src is Indexed/Imm, the extension applies to Src. 
        # If Src is Register but Dst is Indexed, extension applies to Dst.
        
        src_needs_ext = (self.src_reg == 0 and self.as_bits == 3) or (self.as_bits == 1)
        dst_ext_val = self.extension if not src_needs_ext else None
        
        self.dst_str, self.dst_desc = format_dest_operand(self.dst_reg, self.ad_bit, dst_ext_val)

        # Breakdowns
        self.brk_op  = self.yoink(0, 4, Colors.CYAN)
        self.brk_src = self.yoink(4, 8, Colors.GREEN)
        self.brk_ad  = self.yoink(8, 9, Colors.RED)
        self.brk_bw  = self.yoink(9, 10, Colors.YELLOW)
        self.brk_as  = self.yoink(10, 12, Colors.BLUE)
        self.brk_dst = self.yoink(12, 16, Colors.MAGENTA)

        self.rainbow_bin = (
            f"{Colors.CYAN}{self.core[0:4]}{Colors.RESET}"
            f"{Colors.GREEN}{self.core[4:8]}{Colors.RESET}"
            f"{Colors.RED}{self.core[8:9]}{Colors.RESET}"
            f"{Colors.YELLOW}{self.core[9:10]}{Colors.RESET}"
            f"{Colors.BLUE}{self.core[10:12]}{Colors.RESET}"
            f"{Colors.MAGENTA}{self.core[12:16]}{Colors.RESET}"
        )

    def __repr__(self):
        # Determine if we used the extension
        ext_info = ""
        if self.extension is not None:
             ext_info = f"\n [{Colors.ORANGE}EXTENSION{Colors.RESET}] \t{Colors.ORANGE}0x{self.extension:04x}{Colors.RESET}"

        instr_str = (f"{Colors.BOLD}{Colors.CYAN}{self.name}{Colors.YELLOW}{self.suffix} "
                     f"{Colors.GREEN}{self.src_str}{Colors.RESET}, "
                     f"{Colors.MAGENTA}{self.dst_str}{Colors.RESET}")
        
        return (
            f"{Colors.GREY}--------------------------------------------------{Colors.RESET}\n"
            f" {Colors.BOLD}DOUBLE OP{Colors.RESET}   \t{instr_str}\n"
            f"{Colors.GREY}--------------------------------------------------{Colors.RESET}\n"
            f" {Colors.BOLD}BINARY MAP{Colors.RESET}  \t{self.rainbow_bin}\n"
            f"{Colors.GREY}--------------------------------------------------{Colors.RESET}\n"
            f" [{Colors.CYAN}OPCODE{Colors.RESET}]   \t{self.brk_op}\t{Colors.CYAN}{self.name}{Colors.RESET}\n"
            f" [{Colors.GREEN}SRC_REG{Colors.RESET}]  \t{self.brk_src}\t{Colors.GREEN}r{self.src_reg}{Colors.RESET} -> {self.src_desc}\n"
            f" [{Colors.RED}AD_MODE{Colors.RESET}]  \t{self.brk_ad}\t{Colors.RED}bit:{self.ad_bit}{Colors.RESET} -> {self.dst_desc}\n"
            f" [{Colors.YELLOW}B/W{Colors.RESET}]      \t{self.brk_bw}\t{Colors.YELLOW}{bw_mode[self.bw_bit]}{Colors.RESET}\n"
            f" [{Colors.BLUE}AS_MODE{Colors.RESET}]  \t{self.brk_as}\t{Colors.BLUE}bits:{self.as_bits:02b}{Colors.RESET} -> {self.src_desc}\n"
            f" [{Colors.MAGENTA}DST_REG{Colors.RESET}]  \t{self.brk_dst}\t{Colors.MAGENTA}r{self.dst_reg}{Colors.RESET}"
            f"{ext_info}\n"
        )

# --- Format II: Single Operand ---
class SingleOp(InstructionBase):
    def parse(self):
        self.op_bits = (self.opcode >> 7) & 0b111
        self.bw_bit  = (self.opcode >> 6) & 0b1
        self.as_bits = (self.opcode >> 4) & 0b11
        self.dst_reg = self.opcode & 0xF

        self.name = single_opcode_map.get(self.op_bits, "invalid")
        self.suffix = '.b' if self.bw_bit else '.w'
        
        # Single Op Source logic is actually As bits on the "Destination" (Register)
        # SXT r6 -> r6 is accessed via As modes
        self.dst_str, self.dst_desc = format_source_operand(self.dst_reg, self.as_bits, self.extension)

        self.brk_pre = self.yoink(0, 6, Colors.GREY)
        self.brk_op  = self.yoink(6, 9, Colors.CYAN)
        self.brk_bw  = self.yoink(9, 10, Colors.YELLOW)
        self.brk_as  = self.yoink(10, 12, Colors.BLUE)
        self.brk_dst = self.yoink(12, 16, Colors.MAGENTA)

        self.rainbow_bin = (
            f"{Colors.GREY}{self.core[0:6]}{Colors.RESET}"
            f"{Colors.CYAN}{self.core[6:9]}{Colors.RESET}"
            f"{Colors.YELLOW}{self.core[9:10]}{Colors.RESET}"
            f"{Colors.BLUE}{self.core[10:12]}{Colors.RESET}"
            f"{Colors.MAGENTA}{self.core[12:16]}{Colors.RESET}"
        )

    def __repr__(self):
        instr_str = (f"{Colors.BOLD}{Colors.CYAN}{self.name}{Colors.YELLOW}{self.suffix} "
                     f"{Colors.MAGENTA}{self.dst_str}{Colors.RESET}")
        
        ext_info = ""
        if self.extension is not None:
             ext_info = f"\n [{Colors.ORANGE}EXTENSION{Colors.RESET}] \t{Colors.ORANGE}0x{self.extension:04x}{Colors.RESET}"

        return (
            f"{Colors.GREY}--------------------------------------------------{Colors.RESET}\n"
            f" {Colors.BOLD}SINGLE OP{Colors.RESET}   \t{instr_str}\n"
            f"{Colors.GREY}--------------------------------------------------{Colors.RESET}\n"
            f" {Colors.BOLD}BINARY MAP{Colors.RESET}  \t{self.rainbow_bin}\n"
            f"{Colors.GREY}--------------------------------------------------{Colors.RESET}\n"
            f" [{Colors.GREY}PREFIX{Colors.RESET}]   \t{self.brk_pre}\t(fixed)\n"
            f" [{Colors.CYAN}OPCODE{Colors.RESET}]   \t{self.brk_op}\t{Colors.CYAN}{self.name}{Colors.RESET}\n"
            f" [{Colors.YELLOW}B/W{Colors.RESET}]      \t{self.brk_bw}\t{Colors.YELLOW}{bw_mode[self.bw_bit]}{Colors.RESET}\n"
            f" [{Colors.BLUE}AD_MODE{Colors.RESET}]  \t{self.brk_as}\t{Colors.BLUE}bits:{self.as_bits:02b}{Colors.RESET} -> {self.dst_desc}\n"
            f" [{Colors.MAGENTA}DST_REG{Colors.RESET}]  \t{self.brk_dst}\t{Colors.MAGENTA}r{self.dst_reg}{Colors.RESET}"
            f"{ext_info}\n"
        )

# --- Format III: Jumps ---
class JumpOp(InstructionBase):
    def parse(self):
        self.cond_bits = (self.opcode >> 10) & 0b111
        self.offset_raw = self.opcode & 0x3FF
        if self.offset_raw & 0x200: self.offset = self.offset_raw - 1024
        else: self.offset = self.offset_raw
        self.name = jump_opcode_map.get(self.cond_bits, "invalid")
        self.jump_desc = f"$ { '+' if self.offset >= 0 else '' }{self.offset * 2}"

        self.brk_pre = self.yoink(0, 3, Colors.GREY)
        self.brk_cond = self.yoink(3, 6, Colors.CYAN)
        self.brk_off = self.yoink(6, 16, Colors.ORANGE)

        self.rainbow_bin = (
            f"{Colors.GREY}{self.core[0:3]}{Colors.RESET}"
            f"{Colors.CYAN}{self.core[3:6]}{Colors.RESET}"
            f"{Colors.ORANGE}{self.core[6:16]}{Colors.RESET}"
        )

    def __repr__(self):
        return (
            f"{Colors.GREY}--------------------------------------------------{Colors.RESET}\n"
            f" {Colors.BOLD}JUMP OP{Colors.RESET}     \t{Colors.CYAN}{self.name} {Colors.ORANGE}{self.jump_desc}{Colors.RESET}\n"
            f"{Colors.GREY}--------------------------------------------------{Colors.RESET}\n"
            f" {Colors.BOLD}BINARY MAP{Colors.RESET}  \t{self.rainbow_bin}\n"
            f"{Colors.GREY}--------------------------------------------------{Colors.RESET}\n"
            f" [{Colors.GREY}PREFIX{Colors.RESET}]   \t{self.brk_pre}\t(fixed)\n"
            f" [{Colors.CYAN}COND{Colors.RESET}]     \t{self.brk_cond}\t{Colors.CYAN}{self.name}{Colors.RESET}\n"
            f" [{Colors.ORANGE}OFFSET{Colors.RESET}]   \t{self.brk_off}\t{Colors.ORANGE}Decimal: {self.offset}{Colors.RESET}\n"
        )

def get_instruction_parser(val):
    """Factory: Handles 16-bit or 32-bit (Instruction + Extension)."""
    
    # Check if input > 0xFFFF (User provided Instr + Extension)
    # We assume Big-Endian visual input: 0x40391234 -> Instr: 4039, Ext: 1234
    if val > 0xFFFF:
        instr_word = (val >> 16) & 0xFFFF
        ext_word = val & 0xFFFF
    else:
        instr_word = val
        ext_word = None
        
    # JUMP (001...)
    if (instr_word & 0xE000) == 0x2000:
        return JumpOp(instr_word, ext_word)
    # SINGLE (000100...)
    elif (instr_word & 0xFC00) == 0x1000:
        return SingleOp(instr_word, ext_word)
    # DOUBLE (Everything else)
    else:
        return DoubleOp(instr_word, ext_word)

def shitty_menu():
    try:
        raw = input(f'{Colors.BLUE}[MENU]{Colors.RESET} Hex (e.g. {Colors.BOLD}40391234{Colors.RESET} or {Colors.BOLD}5678{Colors.RESET}) or {Colors.RED}q{Colors.RESET} > ')
        if raw.lower().strip() == 'q': return False
        if raw.startswith("0x"): raw = raw[2:]
        
        val = int(raw, 16)
        print(get_instruction_parser(val))
        return True
    except Exception as e:
        print(f"{Colors.RED}[ERROR] {e}{Colors.RESET}")
        return True

if __name__ == "__main__":
    print(f"{Colors.BOLD}--- COMARCH DEBUGGER START ---{Colors.RESET}")
    f = True
    while f: f = shitty_menu()
