package com.barrettotte.models;

import com.barrettotte.models.Building;

import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;

import java.util.List;

@JsonInclude(JsonInclude.Include.NON_NULL)
public class BookStore extends Building {

    private List<String> books;


    @JsonProperty("books")
    public List<String> getBooks() {
        return this.books;
    }
    @JsonProperty("books")
    public void setBooks(final List<String> books) {
        this.books = books;
    }
}
