package com.barrettotte.models.common


import com.fasterxml.jackson.annotation.JsonInclude
import com.fasterxml.jackson.annotation.JsonProperty

@JsonInclude(JsonInclude.Include.NON_NULL)
class Thing {

    @JsonProperty("name")
    String name

}
