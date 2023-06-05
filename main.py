%pip install wikipedia-api
import wikipediaapi
import sys

class Stack:

    def __init__(self, max_size=5):
        self.items = []
        self.max_size = max_size

    def push(self, item):
        if len(self.items) < self.max_size:
            self.items.append(item)
        else:
            raise IndexError("Stack overflow")

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __iter__(self):
        return self

    def __next__(self):
        if not self.is_empty():
            return self.pop()
        else:
            raise StopIteration

s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.pop())

for e in s:
  print(e)

s.push(1)
s.push(2)
s.push(3)

stack_iter = iter(s)

print(next(stack_iter))
print(next(stack_iter))
print(next(stack_iter))

s = Stack()
s.push(1)
s.push(2)
s.push(3)
iterator = iter(s)
while True:
  try:
    e = next(iterator)
    print(e)
  except StopIteration:
    print('Stop')
    break


generator = (x for x in range(10000))
size_generator = sys.getsizeof(generator)
list_comp = [x for x in range(10000)]
size_list_comp = sys.getsizeof(list_comp)
print("generator:", size_generator, "bajtów")
print("list comprehension:", size_list_comp, "bajtów")

def even_numbers(max=6):
  number = 0
  while number <= 6:
    yield number
    number +=2

gen = even_numbers()
print(type(gen))

for e in gen:
  print(e)

def read_wiki_titles(filename: str):
  with open(filename, 'r') as file:
    for line in file:
      yield line.strip()

wik = read_wiki_titles("small.txt")
for e in wik:
  print(e)

wik = read_wiki_titles("small.txt")
title1 = next(wik)
print(title1)

def get_article(title,lang="en"):
  w_api = wikipediaapi.Wikipedia(lang)
  page = w_api.page(title)
  if page.exists():
    return page.text
  else:
    return ""

art = get_article(title1)
print(art)
