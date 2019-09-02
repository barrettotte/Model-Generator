package com.barrettotte.models.common;

import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;

@JsonInclude(JsonInclude.Include.NON_NULL)
public class Person extends Thing {

    private Integer age;


    @JsonProperty("age")
    public Integer getAge() {
        return age;
    }
    @JsonProperty("age")
    public void setAge(final Integer age) {
        this.age = age;
    }
}

