package com.barrettotte.models.common

import com.barrettotte.models.common.Thing

import com.fasterxml.jackson.annotation.JsonInclude
import com.fasterxml.jackson.annotation.JsonProperty

@JsonInclude(JsonInclude.Include.NON_NULL)
class Address extends Thing {

    @JsonProperty("line1")
    String line1

    @JsonProperty("line2")
    String line2

    @JsonProperty("city")
    String city

    @JsonProperty("state")
    String state

    @JsonProperty("zip")
    String zip

}
