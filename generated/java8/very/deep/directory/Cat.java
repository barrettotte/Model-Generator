package com.barrettotte.models.very.deep.directory;

import com.barrettotte.models.common.Thing;

import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;

@JsonInclude(JsonInclude.Include.NON_NULL)
public class Cat extends Thing {

    private String breed;
    private String color;

    public Cat() {
        this.color = "orange";
    }

    @JsonProperty("breed")
    public String getBreed() {
        return this.breed;
    }
    @JsonProperty("breed")
    public void setBreed(final String breed) {
        this.breed = breed;
    }

    @JsonProperty("color")
    public String getColor() {
        return this.color;
    }
    @JsonProperty("color")
    public void setColor(final String color) {
        this.color = color;
    }
}
