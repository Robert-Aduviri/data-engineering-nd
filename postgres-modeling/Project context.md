# Project: Data Modeling with Postgres

## Introduction

A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

The objective is to create a Postgres database with tables designed to optimize queries on song play analysis,
as well as an ETL pipeline that transfers the data from the JSON logs into the database, such that the
analytics team can run queries on it.

The project involves defining fact and dimension tables for a star schema for a particular analytic focus, and writing an ETL pipeline that transfers data from files in two local directories into these tables in Postgres using Python and SQL.
