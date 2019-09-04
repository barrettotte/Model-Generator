package com.barrettotte.models;

import com.barrettotte.models.Book;
import com.barrettotte.models.Building;

import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;

import java.util.List;
import java.util.ArrayList;

@JsonInclude(JsonInclude.Include.NON_NULL)
public class Library extends Building {

    private List<Book> books;

    public Library() {
        this.books = new ArrayList<Book>();
    }

    @JsonProperty("books")
    public List<Book> getBooks() {
        return this.books;
    }
    @JsonProperty("books")
    public void setBooks(final List<Book> books) {
        this.books = books;
    }
}
