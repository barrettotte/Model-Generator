package com.barrettotte.models

import com.barrettotte.models.common.Person
import com.barrettotte.models.common.Thing

import com.fasterxml.jackson.annotation.JsonInclude
import com.fasterxml.jackson.annotation.JsonProperty

import java.math.BigDecimal

@JsonInclude(JsonInclude.Include.NON_NULL)
class Book extends Thing {

    @JsonProperty("genres")
    String[] genres = new String[10]

    @JsonProperty("pageLength")
    long pageLength = 25L

    @JsonProperty("isbn")
    String isbn

    @JsonProperty("author")
    Person author = new Person()

    @JsonProperty("price")
    BigDecimal price = new BigDecimal(0)

}
