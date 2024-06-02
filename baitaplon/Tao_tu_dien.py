import sys
import io
import os

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')

class LinkedListNode:
    def __init__(self, word_type, meaning, example):
        self.word_type = word_type
        self.meaning = meaning
        self.example = example
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_ordered(self, word_type, meaning, example):
        new_node = LinkedListNode(word_type, meaning, example)
        if not self.head or self.head.word_type > word_type:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.word_type <= word_type:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

class BSTNode:
    def __init__(self, word):
        self.word = word
        self.meanings = LinkedList()
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, word):
        if not self.root:
            self.root = BSTNode(word)
        else:
            self._insert(self.root, word)

    def _insert(self, node, word):
        if word < node.word:
            if node.left is None:
                node.left = BSTNode(word)
            else:
                self._insert(node.left, word)
        elif word > node.word:
            if node.right is None:
                node.right = BSTNode(word)
            else:
                self._insert(node.right, word)

    def find(self, word):
        return self._find(self.root, word)

    def _find(self, node, word):
        if node is None or node.word == word:
            return node
        elif word < node.word:
            return self._find(node.left, word)
        else:
            return self._find(node.right, word)

    def delete(self, word):
        self.root = self._delete(self.root, word)

    def _delete(self, node, word):
        if node is None:
            return node
        if word < node.word:
            node.left = self._delete(node.left, word)
        elif word > node.word:
            node.right = self._delete(node.right, word)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            min_larger_node = self._min_value_node(node.right)
            node.word = min_larger_node.word
            node.right = self._delete(node.right, min_larger_node.word)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder(self):
        return self._inorder(self.root)

    def _inorder(self, node):
        if node:
            yield from self._inorder(node.left)
            yield node
            yield from self._inorder(node.right)

class HashTable:
    def __init__(self, size=26):
        self.size = size
        self.table = [BST() for _ in range(size)]

    def _hash(self, word):
        return ord(word[0].lower()) - ord('a')

    def insert(self, word):
        index = self._hash(word)
        self.table[index].insert(word)

    def find(self, word):
        index = self._hash(word)
        return self.table[index].find(word)

    def delete(self, word):
        index = self._hash(word)
        self.table[index].delete(word)

    def all_words(self):
        for bst in self.table:
            yield from bst.inorder()

def input_word(prompt):
    while True:
        try:
            word = input(f'Enter {prompt}: ').strip()
            if all(char.isalpha() or char.isspace() for char in word):
                return word
            else:
                print('This is not a valid word. Please re-enter.')
        except Exception as err:
            print('Error:', err)

def input_number():
    while True:
        try:
            n = int(input('Select a function to perform (0-4): '))
            if 0 <= n <= 4:
                return n
            else:
                print('This is not a valid number between 0-4. Please re-enter.')
        except ValueError:
            print('Please enter a valid number.')
        except Exception as err:
            print('Error:', err)

def add_word(dictionary):
    print('\t1.- Add word')
    word = input_word('new word')
    meanings = []
    while True:
        word_type = input_word('word type (noun, verb, adjective, etc.)')
        meaning = input_word('meaning')
        example = input_word('example')
        meanings.append((word_type, meaning, example))
        if input('Add another meaning for this word? (Y/N): ').strip().upper() != 'Y':
            break
    node = dictionary.find(word)
    if not node:
        dictionary.insert(word)
        node = dictionary.find(word)
    for word_type, meaning, example in meanings:
        node.meanings.insert_ordered(word_type, meaning, example)
    print('New word has been added.')

def find_word(dictionary):
    print('\t2.- Find word')
    word = input_word('word to find')
    node = dictionary.find(word)
    if node:
        print(f'Found word: {word}')
        for meaning in node.meanings:
            print(f'    Type    : {meaning.word_type}')
            print(f'    Meaning : {meaning.meaning}')
            print(f'    Example : {meaning.example}')
    else:
        print(f'Word "{word}" not found in the dictionary.')

def delete_word(dictionary):
    print('\t3.- Delete word')
    word = input_word('word to delete')
    if dictionary.find(word):
        dictionary.delete(word)
        print('Word has been deleted.')
    else:
        print(f'Word "{word}" not found.')

def view_all(dictionary):
    print('\t4.- View all')
    if not any(dictionary.all_words()):
        print('Your dictionary currently has no words. You need to add new words.')
    else:
        print('Your dictionary:')
        for node in dictionary.all_words():
            print(f'Word: {node.word}')
            for meaning in node.meanings:
                print(f'    Type    : {meaning.word_type}')
                print(f'    Meaning : {meaning.meaning}')
                print(f'    Example : {meaning.example}')
            print()

def menu():
    print('-' * 40)
    print('DICTIONARY PROGRAM'.center(40, '*'))
    print('-' * 40)
    print('\t1.- Add word')
    print('\t2.- Find word')
    print('\t3.- Delete word')
    print('\t4.- View all')
    print('\t0.- Press 0 to exit the program')

def save_dictionary(file_name, dictionary):
    with open(file_name, 'w', encoding='utf-8') as file:
        for node in dictionary.all_words():
            file.write(node.word)
            meanings = '|'.join(f"{meaning.word_type},{meaning.meaning},{meaning.example}" for meaning in node.meanings)
            file.write(f",{meanings}\n")

def load_dictionary(file_name):
    if not os.path.exists(file_name):
        return HashTable()
    dictionary = HashTable()
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split(',')
            word = parts[0]
            dictionary.insert(word)
            node = dictionary.find(word)
            for meaning in parts[1].split('|'):
                word_type, meaning, example = meaning.split(',')
                node.meanings.insert_ordered(word_type, meaning, example)
    return dictionary

def main():
    file_name = "mãsinhviên_bam.txt"
    dictionary = load_dictionary(file_name)
    while True:
        menu()
        choice = input_number()
        if choice == 0:
            print('Dictionary program ended')
            save_dictionary(file_name, dictionary)
            break
        elif choice == 1:
            add_word(dictionary)
        elif choice == 2:
            find_word(dictionary)
        elif choice == 3:
            delete_word(dictionary)
        elif choice == 4:
            view_all(dictionary)

if __name__ == "__main__":
    main()
