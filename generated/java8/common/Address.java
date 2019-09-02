package com.barrettotte.models.common;

import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;

@JsonInclude(JsonInclude.Include.NON_NULL)
public class Address extends Thing {

    private String line1;

    private String line2;

    private String city;

    private String state;

    private String zip;


    @JsonProperty("line1")
    public String getLine1() {
        return line1;
    }
    @JsonProperty("line1")
    public void setLine1(final String line1) {
        this.line1 = line1;
    }

    @JsonProperty("line2")
    public String getLine2() {
        return line2;
    }
    @JsonProperty("line2")
    public void setLine2(final String line2) {
        this.line2 = line2;
    }

    @JsonProperty("city")
    public String getCity() {
        return city;
    }
    @JsonProperty("city")
    public void setCity(final String city) {
        this.city = city;
    }

    @JsonProperty("state")
    public String getState() {
        return state;
    }
    @JsonProperty("state")
    public void setState(final String state) {
        this.state = state;
    }

    @JsonProperty("zip")
    public String getZip() {
        return zip;
    }
    @JsonProperty("zip")
    public void setZip(final String zip) {
        this.zip = zip;
    }
}

