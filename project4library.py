# ===== Starter Template: Library Management System =====
# Suggested structure:
# src/models.py -> Book, Member, BorrowRecord, FinePolicy
# src/library.py -> Library class (business logic)
# cli.py -> menu (I/O only)

# tests/test_*.py -> unit tests
from __future__ import annotations
from dataclasses import dataclass, field
from enum import member
from typing import Dict, List, Optional, Set
from abc import ABC, abstractmethod
from datetime import date
# ---------- Policy (Abstraction) ----------
class FinePolicy(ABC):
 @abstractmethod
 def calculate(self, days_late: int) -> float:
     ...
class SimpleFinePolicy(FinePolicy):
 def __init__(self, per_day: float = 5.0):
  self.per_day = per_day
  
def calculate(self, days_late: int) -> float:
# TODO: return fine for late days (no negative)
  raise NotImplementedError
# ---------- Data Models ----------
@dataclass
class Book:
 book_id: str
 title: str
 author: str
__available: bool = field(default=True, repr=False)

def borrow(self) -> None:
# TODO: if not available -> raise ValueError
# TODO: set available False
 raise NotImplementedError

def return_book(self) -> None:
# TODO: set available True
 raise NotImplementedError

def is_available(self) -> bool:
 return self.__available

@dataclass
class Member:
    member_id : str
    name : str
    __borrowed_books: set[str] = field(default_factory= set, repr=False)
    
    def borrow_book(self, book_id : str, lim: int = 3) ->None:
        # TODO enforce limit, then add
        raise NotImplementedError
    
    def return_book(self, book_id: str) -> None:
        # TODO: validate membership, then remove
       raise NotImplementedError
    
    @property
    def borrowed_books(self) ->set[str]:
        return set(self.__borrowed_books)
@dataclass
class Borrowrecord:
    member_id : str   
    book_id = str
    borrow_date: date
    return_date: Optional[date] = None

#--------------- Main Bussiness Class ---------------
class Library:
    def __init__(self, fine_policy: FinePolicy):
        self.finepolicy = FinePolicy
        self.books = Dict[str, Book] = {}
        self.members = Dict[str, Member] = {}
        self.records = List[Borrowrecord] = []

    def add_book(self, book_id: str, title: str, author: str) -> None:
       # TODO: unique ID check, then add Book
      raise NotImplementedError
    def add_member(self, member_id: str, name: str) -> None:
       # TODO: unique ID check, then add Member
     raise NotImplementedError
 
    def borrow_book(self, member_id: str, book_id: str, borrow_date: date) -> None:
    # TODO:
    # 1) validate IDs exist
    # 2) book.borrow()
    # 3) member.borrow_book(book_id)
    # 4) append BorrowRecord
      raise NotImplementedError
 
    def return_book(self, member_id: str, book_id: str, return_date: date) -> float:
    # TODO:
    # 1) validate IDs exist
    # 2) member.return_book(book_id)
    # 3) book.return_book()
    # 4) find open record and close it (set return_date)
    # 5) compute fine using policy and return it
     raise NotImplementedError        
        
         
     
    
    
            
    
        
                
    