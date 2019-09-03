package com.barrettotte.models.very.deep.directory

import com.barrettotte.models.common.Thing

import com.fasterxml.jackson.annotation.JsonInclude
import com.fasterxml.jackson.annotation.JsonProperty

@JsonInclude(JsonInclude.Include.NON_NULL)
class Cat extends Thing {

    @JsonProperty("breed")
    String breed

    @JsonProperty("color")
    String color = "orange"

}
