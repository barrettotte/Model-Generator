package com.barrettotte.models;

import com.barrettotte.models.common.Thing;

import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;

@JsonInclude(JsonInclude.Include.NON_NULL)
public class Building extends Thing {

    private Object address;


    @JsonProperty("address")
    public Object getAddress() {
        return this.address;
    }
    @JsonProperty("address")
    public void setAddress(final Object address) {
        this.address = address;
    }
}
