package com.barrettotte.models;

import com.barrettotte.models.common.Thing;

import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;

@JsonInclude(JsonInclude.Include.NON_NULL)
public class Book extends Thing {

    private String genre;

    private float pageLength;

    private String isbn;

    private Object author;


    @JsonProperty("genre")
    public String getGenre() {
        return genre;
    }
    @JsonProperty("genre")
    public void setGenre(final String genre) {
        this.genre = genre;
    }

    @JsonProperty("pageLength")
    public float getPagelength() {
        return pageLength;
    }
    @JsonProperty("pageLength")
    public void setPagelength(final float pageLength) {
        this.pageLength = pageLength;
    }

    @JsonProperty("isbn")
    public String getIsbn() {
        return isbn;
    }
    @JsonProperty("isbn")
    public void setIsbn(final String isbn) {
        this.isbn = isbn;
    }

    @JsonProperty("author")
    public Object getAuthor() {
        return author;
    }
    @JsonProperty("author")
    public void setAuthor(final Object author) {
        this.author = author;
    }
}



package com.barrettotte.models;

import com.barrettotte.models.common.Thing;

import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;

@JsonInclude(JsonInclude.Include.NON_NULL)
public class Building extends Thing {




}



package com.barrettotte.models;

import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;

@JsonInclude(JsonInclude.Include.NON_NULL)
public class Library extends Building {




}



package com.barrettotte.models;

import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;

@JsonInclude(JsonInclude.Include.NON_NULL)
public class Bookstore extends Building {




}



package com.barrettotte.models.common;

import com.barrettotte.models.Thing;

import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;

@JsonInclude(JsonInclude.Include.NON_NULL)
public class Person extends Thing {




}



package com.barrettotte.models.common;

import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;

@JsonInclude(JsonInclude.Include.NON_NULL)
public class Thing {

    private String name;


    @JsonProperty("name")
    public String getName() {
        return name;
    }
    @JsonProperty("name")
    public void setName(final String name) {
        this.name = name;
    }
}



package com.barrettotte.models.very.deep.directory;

import com.barrettotte.models.common.Thing;

import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;

@JsonInclude(JsonInclude.Include.NON_NULL)
public class Cat extends Thing {

    private String breed;

    private String color;


    @JsonProperty("breed")
    public String getBreed() {
        return breed;
    }
    @JsonProperty("breed")
    public void setBreed(final String breed) {
        this.breed = breed;
    }

    @JsonProperty("color")
    public String getColor() {
        return color;
    }
    @JsonProperty("color")
    public void setColor(final String color) {
        this.color = color;
    }
}



