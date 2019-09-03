package com.barrettotte.models

import com.barrettotte.models.common.Address
import com.barrettotte.models.common.Thing

import com.fasterxml.jackson.annotation.JsonInclude
import com.fasterxml.jackson.annotation.JsonProperty

@JsonInclude(JsonInclude.Include.NON_NULL)
class Building extends Thing {

    @JsonProperty("address")
    Address address = new Address()

}
