from getch import getch
from sys import stdout


class Brainfuck:
    def __init__(self):
        self.cells = bytearray(1)
        self.dp = 0  # data pointer
        self.ip = 0  # instruction pointer

    def increment_cell(self, flag):
        try:
            self.cells[self.dp] += 1 * flag
        except ValueError:
            self.cells[self.dp] = int(256 % (255.5 + flag * 0.5))

    def skip(self, flag, code):
        chars = ["", "[", "]"]
        nest_incrementer = chars[flag]
        nest_decrementer = chars[flag * -1]
        nest_counter = 1
        while nest_counter > 0:
            self.ip += 1 * flag
            if code[self.ip] == nest_incrementer:
                nest_counter += 1
            if code[self.ip] == nest_decrementer:
                nest_counter -= 1

    def execute_instruction(self, instruction, code):
        if instruction == ">":
            self.dp += 1
        if instruction == "<":
            self.dp -= 1
            if self.dp == -1:
                self.dp = len(self.cells)
        if instruction == "+":
            self.increment_cell(1)
        if instruction == "-":
            self.increment_cell(-1)
        if instruction == "[":
            if self.cells[self.dp] == 0:
                self.skip(1, code)
        if instruction == "]":
            if self.cells[self.dp] != 0:
                self.skip(-1, code)
        if instruction == ",":
            self.cells[self.dp] = ord(getch())
        if instruction == ".":
            stdout.write(chr(self.cells[self.dp]))

    def show_cells(self):
        print(" ".join([f"[{hex(cell)}]" for cell in self.cells]))

    def main(self, code):
        while self.ip < len(code):
            while len(self.cells) <= self.dp:
                self.cells.append(0)
            self.execute_instruction(code[self.ip], code)
            self.ip += 1
