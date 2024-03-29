"""
A regular expression is used to describe a set of strings. For this problem the alphabet is limited to 'a' and 'b'.
We define R to be valid regular expression if:
1) R is "a" or "b".
2) R is of the form "(R_1R_2)" where R_1 and R_2 is a valid regular expression.
3) R is of the form "(R_1|R_2)" where R_1 and R_2 is a valid regular expression.
4) R is of the form "(R_1*)" where R_1 is a valid regular expression.
Regular expressions can be nested and wull always have two elements in the parentheses.
('*' is an element, '|' is not; basically, there will always be pairwise evaluation) Additionally, '*' will always be the second element . '(*a)' is invalid.
The set of strings recognized by R are as follows:
1) If R is "a" then the set of strings recognized = a.
2) If R is "b" then the set of strings recognized = b.
3) If R is of the form "(R_1R_2)" then the set of strings recognized = {xy | x is a string recognized by R_1 and y is a string recognized by R_2}.
4) If R is of the form "(R_1|R_2)" then the set of strings recognized = {x | x is a string recognized by R_1 or x is a string recognized by R_2}.
5) If R is of the form "(R_1*)" then the set of strings recognized = {x_1x_2...x_k | k >= 0 and each x_i is a string recognized by R_1}.
Task
Given a regular expression and an integer, L, count how many strings of length L are recognized by it.
Constraints
1<=T<=50
1<= |R| <= 100
1<=L<=100
it is guaranteed that R will conform to the definition provided above.
"""
from enum import Enum
from collections import namedtuple

Edge = namedtuple('Edge', 'dest char')

class Alphabet(Enum):
    a = 'a'
    b = 'b'
    e = None


def empty_edge(dest):
    return Edge(dest, Alphabet.e)


class CountStrings:
    def __init__(self, regex_string):
        RegexGraphNFA.node_count = 0
        self.regex_string = regex_string
        nfa_graph = self.translate_regex()
        translate_graph = TranslateGraph(nfa_graph)
        self.dfa_graph = translate_graph.translate()

    def calculate(self, string_length):
        return self.dfa_graph.count_paths(string_length)

    def translate_regex(self, index=0):
        result_set = ResultSet()
        while index < len(self.regex_string):
            if self.regex_string[index] == '(':
                out_list, index = self.translate_regex(index + 1)
                result_set.insert(out_list)
            elif self.regex_string[index] == ')':
                result = result_set.calculate_result()
                return result, index
            elif self.regex_string[index] == '|':
                result_set.set_or()
            elif self.regex_string[index] == '*':
                result_set.set_repeat()
            else:
                result_set.insert(RegexGraphNFA(Alphabet[self.regex_string[index]]))
            index += 1
        return result_set.calculate_result()


class ResultSet:
    AND, OR, REPEAT = 1, 2, 3

    def __init__(self):
        self.r1 = None
        self.r2 = None
        self.op = self.AND

    def set_or(self):
        self.op = self.OR

    def set_repeat(self):
        self.op = self.REPEAT

    def calculate_result(self):
        if self.op == self.REPEAT:
            self.calculate_repeat()
        elif self.r2 is None:
            pass
        elif self.op == self.OR:
            self.calculate_or()
        else:
            self.calculate_and()
        return self.r1

    def calculate_repeat(self):
        self.r1.graph_repeat()

    def calculate_or(self):
        self.r1.graph_or(self.r2)

    def calculate_and(self):
        self.r1.graph_add(self.r2)

    def insert(self, value):
        if self.r1 is None:
            self.r1 = value
        else:
            self.r2 = value


class RegexGraphNFA:
    node_count = 0

    def __init__(self, in_char):
        self.edges = None
        self.head = None
        self.tail = None
        self.insert_char(in_char)

    @classmethod
    def get_next_node_id(cls):
        node_id = cls.node_count
        cls.node_count += 1
        return node_id

    def insert_char(self, value):
        self.head = self.get_next_node_id()
        self.tail = self.get_next_node_id()
        self.edges = {self.head: [Edge(self.tail, value)],
                      self.tail: []}

    def graph_add(self, other):
        join_node = self.get_next_node_id()
        self.join(other)
        self.edges[self.tail].append(empty_edge(join_node))
        self.edges[join_node] = [empty_edge(other.head)]
        self.tail = other.tail

    def graph_repeat(self):
        new_head = self.get_next_node_id()
        new_tail = self.get_next_node_id()
        self.edges[self.tail].extend([empty_edge(self.head), empty_edge(new_tail)])
        self.edges[new_head] = [empty_edge(self.head), empty_edge(new_tail)]
        self.edges[new_tail] = []
        self.head = new_head
        self.tail = new_tail

    def graph_or(self, other):
        new_head = self.get_next_node_id()
        new_tail = self.get_next_node_id()
        self.join(other)
        self.edges[new_head] = [empty_edge(self.head), empty_edge(other.head)]
        self.edges[self.tail].append(empty_edge(new_tail))
        self.edges[other.tail].append(empty_edge(new_tail))
        self.edges[new_tail] = []
        self.head = new_head
        self.tail = new_tail

    def join(self, other):
        for node, edge in other.edges.items():
            if node in self.edges:
                self.edges[node].extend(edge)
            else:
                self.edges[node] = edge

    def get_dfa_char_node_set(self, origin, use_char):
        node_set = set()
        for my_node in origin:
            for edges in self.edges[my_node]:
                if edges.char == use_char:
                    node_set.add(edges.dest)

        return self.get_dfa_zero_node_set(node_set)

    def get_dfa_zero_node_set(self, origin):
        node_set = set(origin)
        processed = set()
        while len(node_set.difference(processed)) > 0:
            my_node = node_set.difference(processed).pop()
            for edges in self.edges[my_node]:
                if edges.char == Alphabet.e:
                    node_set.add(edges.dest)
            processed.add(my_node)
        return frozenset(node_set)


class TranslateGraph:
    language = (Alphabet.a, Alphabet.b)

    def __init__(self, nfa_graph: RegexGraphNFA):
        self.node_count = 0
        self.nfa_graph = nfa_graph
        self.trans_to = {}
        self.trans_from = {}
        self.table = {}

    def get_next_node_id(self):
        node_id = self.node_count
        self.node_count += 1
        return node_id

    def add_translate(self, nfa_ids):
        if len(nfa_ids) == 0:
            return None
        if nfa_ids not in self.trans_from:
            dfa_id = self.get_next_node_id()
            self.trans_to[dfa_id] = nfa_ids
            self.trans_from[nfa_ids] = dfa_id
            self.table[dfa_id] = dict(zip(self.language, [None] * len(self.language)))
        return self.trans_from[nfa_ids]

    def translate(self):
        self.create_translate_table()
        return self.build_dfa()

    def build_dfa(self):
        head = 0
        valid_ends = set()
        adjacency = {}
        for node, edges in self.table.items():
            adjacency[node] = []
            if self.nfa_graph.tail in self.trans_to[node]:
                valid_ends.add(node)
            for my_char, node_dest in edges.items():
                if node_dest is not None:
                    adjacency[node].append(Edge(node_dest, my_char))
        return RegexGraphDFA(head, valid_ends, adjacency)

    def create_translate_table(self):
        nfa_ids = self.nfa_graph.get_dfa_zero_node_set({self.nfa_graph.head})
        self.add_translate(nfa_ids)
        processed = set()

        while len(set(self.table).difference(processed)) > 0:
            my_node = set(self.table).difference(processed).pop()
            for char in self.language:
                next_nodes = self.nfa_graph.get_dfa_char_node_set(self.trans_to[my_node], char)
                dfa_id = self.add_translate(next_nodes)
                self.table[my_node][char] = dfa_id
            processed.add(my_node)


class RegexGraphDFA:
    def __init__(self, head, valid_ends, edges):
        self.edges = edges
        self.head = head
        self.valid_ends = valid_ends
        self.edge_matrix = Matrix.get_from_edges(len(self.edges), self.edges)

    def count_paths(self, length):
        modulo = 1000000007
        if length == 0:
            return 0 if 0 not in self.valid_ends else 1
        edge_walk = self.edge_matrix.pow(length, modulo)
        count = 0
        for end_node in self.valid_ends:
            count += edge_walk.matrix[self.head][end_node]
        return count % modulo


class Matrix:
    @staticmethod
    def get_from_edges(dimension, adj_list):
        my_matrix = Matrix.get_zeros(dimension)
        my_matrix.add_edges(adj_list)
        return my_matrix

    @staticmethod
    def get_zeros(dimension):
        my_matrix = Matrix(dimension)
        my_matrix.pad_zeros()
        return my_matrix

    def copy(self):
        my_matrix = Matrix(self.dimension)
        my_matrix.matrix = []
        for i in range(self.dimension):
            my_matrix.matrix.append([])
            for j in range(self.dimension):
                my_matrix.matrix[i].append(self.matrix[i][j])
        return my_matrix

    def __init__(self, dimension):
        self.matrix = None
        self.dimension = dimension

    def __str__(self):
        my_str = ''
        for row in self.matrix:
            my_str += str(row) + "\n"
        return my_str

    def pad_zeros(self):
        self.matrix = []
        for i in range(self.dimension):
            self.matrix.append([])
            for j in range(self.dimension):
                self.matrix[i].append(0)

    def add_edges(self, adj_list):
        if adj_list is not None:
            for from_node, edge_list in adj_list.items():
                for to_node, my_char in edge_list:
                    self.matrix[from_node][to_node] = 1

    def pow(self, pow_val, mod_val=None):
        started = False
        current_pow = 1
        current_val = 0
        while pow_val > 0:
            if current_pow == 1:
                current_pow_matrix = self.copy()
            else:
                current_pow_matrix = current_pow_matrix.mat_square_mult(current_pow_matrix, mod_val)
            if pow_val % (2 * current_pow):
                current_val += current_pow
                if started:
                    result = result.mat_square_mult(current_pow_matrix, mod_val)
                else:
                    result = current_pow_matrix.copy()
                    started = True
                pow_val -= current_pow
            current_pow *= 2
        return result

    def mat_square_mult(self, other, mod_val=None):
        result = Matrix.get_zeros(self.dimension)
        for i in range(self.dimension):
            for j in range(self.dimension):
                val = 0
                for k in range(self.dimension):
                    val += self.matrix[i][k] * other.matrix[k][j]
                if mod_val is not None:
                    val %= mod_val
                result.matrix[i][j] = val

        return result


def main():
    cases = int(input().strip())
    for i in range(cases):
        in_line = input().strip().split()
        my_class = CountStrings(in_line[0])
        print(my_class.calculate(int(in_line[1])))


if __name__ == "__main__":
    main()