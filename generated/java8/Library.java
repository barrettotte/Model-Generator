package com.barrettotte.models;

import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;

@JsonInclude(JsonInclude.Include.NON_NULL)
public class Library extends Building {

    private Set<String> books;


    @JsonProperty("books")
    public Set<String> getBooks() {
        return books;
    }
    @JsonProperty("books")
    public void setBooks(final Set<String> books) {
        this.books = books;
    }
}

