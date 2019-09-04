package com.barrettotte.models.common;


import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;

@JsonInclude(JsonInclude.Include.NON_NULL)
public class Thing {

    private String name;

    public Thing() {
    }

    @JsonProperty("name")
    public String getName() {
        return this.name;
    }
    @JsonProperty("name")
    public void setName(final String name) {
        this.name = name;
    }
}
