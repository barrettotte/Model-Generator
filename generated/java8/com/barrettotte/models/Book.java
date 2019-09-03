package com.barrettotte.models;

import com.barrettotte.models.common.Person;
import com.barrettotte.models.common.Thing;

import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;

import java.math.BigDecimal;

@JsonInclude(JsonInclude.Include.NON_NULL)
public class Book extends Thing {

    private String[] genres;
    private long pageLength;
    private String isbn;
    private Person author;
    private BigDecimal price;

    public Book() {
        this.genres = new String[10];
        this.pageLength = 25L;
        this.author = new Person();
        this.price = new BigDecimal(0);
    }

    @JsonProperty("genres")
    public String[] getGenres() {
        return this.genres;
    }
    @JsonProperty("genres")
    public void setGenres(final String[] genres) {
        this.genres = genres;
    }

    @JsonProperty("pageLength")
    public long getPageLength() {
        return this.pageLength;
    }
    @JsonProperty("pageLength")
    public void setPageLength(final long pageLength) {
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
    public Person getAuthor() {
        return this.author;
    }
    @JsonProperty("author")
    public void setAuthor(final Person author) {
        this.author = author;
    }

    @JsonProperty("price")
    public BigDecimal getPrice() {
        return this.price;
    }
    @JsonProperty("price")
    public void setPrice(final BigDecimal price) {
        this.price = price;
    }
}
