package com.barrettotte.models

import com.barrettotte.models.Book
import com.barrettotte.models.Building

import com.fasterxml.jackson.annotation.JsonInclude
import com.fasterxml.jackson.annotation.JsonProperty

import java.util.List
import java.util.ArrayList

@JsonInclude(JsonInclude.Include.NON_NULL)
class Library extends Building {

    @JsonProperty("books")
    List<Book> books = new ArrayList<Book>()

}
