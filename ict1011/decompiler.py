import sys

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'    
    GREEN = '\033[92m'   
    YELLOW = '\033[93m'  
    MAGENTA = '\033[95m' 
    RED = '\033[91m'
    GREY = '\033[90m'    
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

single_opcode_table = {
    0b000: 'rrc',
    0b001: 'swpb',
    0b010: 'rra',
    0b011: 'sxt',
    0b100: 'push',
    0b101: 'call',
    0b110: 'reti'
}

mode = {
    0b0: 'word',
    0b1: 'byte'
}

addr_mode = {
    0b00: 'register',
    0b01: 'indexed',
    0b10: 'indirect register',
    0b11: 'indirect autoincrement',
}

class SingleOp:
    def __init__(self, opcode: int):
        self.opcode = opcode & 0xFFFF
        self.parse_opcode()

    def yoink(self, start, end, color_code):
        val = self.core[start:end]
        return (f"{Colors.GREY}{'.' * start}{Colors.RESET}"
                f"{color_code}{val}{Colors.RESET}"
                f"{Colors.GREY}{'.' * (16-end)}{Colors.RESET}")

    def parse_opcode(self):
        self.core = bin(self.opcode)[2:].zfill(16)
        self.opcode_idx = (self.opcode >> 7) & 0b111
        self.name = single_opcode_table.get(self.opcode_idx, "invalid")
        self.byte_mode = bool((self.opcode >> 6) & 0b1)
        self.suffix = '.b' if self.byte_mode else '.w'
        self.as_mode = (self.opcode >> 4) & 0b11
        self.reg_val = self.opcode & 0xF
        self.src = f'r{self.reg_val}'

        self.rainbow_bin = (
            f"{Colors.GREY}{self.core[0:6]}{Colors.RESET}"
            f"{Colors.CYAN}{self.core[6:9]}{Colors.RESET}"
            f"{Colors.YELLOW}{self.core[9:10]}{Colors.RESET}"
            f"{Colors.GREEN}{self.core[10:12]}{Colors.RESET}"
            f"{Colors.MAGENTA}{self.core[12:16]}{Colors.RESET}"
        )

        self.brk_prefix    = self.yoink(0, 6, Colors.GREY)
        self.brk_opcode    = self.yoink(6, 9, Colors.CYAN)
        self.brk_mode      = self.yoink(9, 10, Colors.YELLOW)
        self.brk_addr_mode = self.yoink(10, 12, Colors.GREEN)
        self.brk_operand   = self.yoink(12, 16, Colors.MAGENTA)

    def __repr__(self):
        instr_str = f"{Colors.BOLD}{Colors.CYAN}{self.name}{Colors.YELLOW}{self.suffix} {Colors.MAGENTA}{self.src}{Colors.RESET}"
        
        return (
            f"{Colors.GREY}--------------------------------------------------{Colors.RESET}\n"
            f" {Colors.BOLD}INSTRUCTION{Colors.RESET} \t{instr_str}\n"
            f"{Colors.GREY}--------------------------------------------------{Colors.RESET}\n"
            f" {Colors.BOLD}BINARY MAP{Colors.RESET}  \t{self.rainbow_bin}\n"
            f"{Colors.GREY}--------------------------------------------------{Colors.RESET}\n"
            f" [{Colors.GREY}PREFIX{Colors.RESET}]   \t{self.brk_prefix}\t(fixed)\n"
            f" [{Colors.CYAN}OPCODE{Colors.RESET}]   \t{self.brk_opcode}\t{Colors.CYAN}{self.name}{Colors.RESET}\n"
            f" [{Colors.YELLOW}B/W{Colors.RESET}]      \t{self.brk_mode}\t{Colors.YELLOW}{mode[self.byte_mode]}{Colors.RESET}\n"
            f" [{Colors.GREEN}AD_MODE{Colors.RESET}]  \t{self.brk_addr_mode}\t{Colors.GREEN}{addr_mode[self.as_mode]}{Colors.RESET}\n"
            f" [{Colors.MAGENTA}OPERAND{Colors.RESET}]  \t{self.brk_operand}\t{Colors.MAGENTA}{self.src}{Colors.RESET}\n"
        )

def shitty_menu():
    try:
        raw = input(f'{Colors.BLUE}[MENU]{Colors.RESET} the decoderrrr (e.g. {Colors.BOLD}0x120f{Colors.RESET}) or {Colors.RED}q{Colors.RESET} to quit > ')
        if raw.lower().strip() == 'q':
            print(f"{Colors.RED}Exiting...{Colors.RESET}")
            return False
        if raw.startswith("0x"):
            raw = raw[2:]
        val = int(raw, 16)
        if (val & 0xFC00) != 0x1000:
            pass

        print(SingleOp(val))
        return True
    except:
        import traceback; traceback.print_exc()

print(f"{Colors.BOLD}--- break it down for me ---{Colors.RESET}")
f = True
while f:
    f = shitty_menu()
