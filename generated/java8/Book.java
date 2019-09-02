package com.barrettotte.models;

import com.barrettotte.models.common.Thing;

import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;

@JsonInclude(JsonInclude.Include.NON_NULL)
public class Book extends Thing {

    private String genre;
    private Float pageLength;
    private String isbn;
    private Object author;


    @JsonProperty("genre")
    public String getGenre() {
        return this.genre;
    }
    @JsonProperty("genre")
    public void setGenre(final String genre) {
        this.genre = genre;
    }

    @JsonProperty("pageLength")
    public Float getPageLength() {
        return this.pageLength;
    }
    @JsonProperty("pageLength")
    public void setPageLength(final Float pageLength) {
        this.pageLength = pageLength;
    }

    @JsonProperty("isbn")
    public String getIsbn() {
        return this.isbn;
    }
    @JsonProperty("isbn")
    public void setIsbn(final String isbn) {
        this.isbn = isbn;
    }

    @JsonProperty("author")
    public Object getAuthor() {
        return this.author;
    }
    @JsonProperty("author")
    public void setAuthor(final Object author) {
        this.author = author;
    }
}
