package com.barrettotte.models

import com.barrettotte.models.Book
import com.barrettotte.models.Building

import com.fasterxml.jackson.module.kotlin.*

@JsonInclude(JsonInclude.Include.NON_NULL)
open class Library : Building {
    var books: List<Book> = MutableList<Book>()
}
