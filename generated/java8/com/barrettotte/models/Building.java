package com.barrettotte.models;

import com.barrettotte.models.common.Address;
import com.barrettotte.models.common.Thing;

import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;

@JsonInclude(JsonInclude.Include.NON_NULL)
public class Building extends Thing {

    private Address address;

    public Building() {
        this.address = new Address();
    }

    @JsonProperty("address")
    public Address getAddress() {
        return this.address;
    }
    @JsonProperty("address")
    public void setAddress(final Address address) {
        this.address = address;
    }
}
