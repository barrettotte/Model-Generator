package com.barrettotte.models.common

import com.barrettotte.models.common.Thing

import com.fasterxml.jackson.annotation.JsonInclude
import com.fasterxml.jackson.annotation.JsonProperty

@JsonInclude(JsonInclude.Include.NON_NULL)
class Person extends Thing {

    @JsonProperty("age")
    Integer age

}
