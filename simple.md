---
title: "First Steps to Quarto"
format:
 pdf:
    documentclass: report
    template-partials:
      - before-body.tex
      - toc.tex
    include-in-header:
     - text: |
          \usepackage[sfdefault]{carlito}
          \usepackage[a4paper, total={184.6mm, 271.6mm}]{geometry} % Set the page size
          \usepackage{scrlayer-scrpage}
          \lofoot{MAX FORDHAM}
          \rofoot{\thepage}
          
jupyter: python3
---

## Heading 2

### Heading 3

## Inline Text Formatting

**strong**, _emphasis_, `literal text`, \*escaped symbols\*

## Line Breaks

Fleas \
Adam \
Had 'em.

## Bullet points and numbered lists

- Lists can start with `-` or `*`
  - My other, nested
  - bullet point list!

1. My numbered list
2. has two points

By Strickland Gillilan

## Images

![Some red dot](images/some_red_dot.png){width=30mm}


## Tables

| foo            | bar            |
|----------------|----------------|
| baz            | bim            |
| test test test | bim            |
| baz            | bim            |
| baz            | test test test |
| baz            | bim            |
| baz            | bim            |
| test test test | bim            |
| baz            | bim            |
| baz            | test test test |
| baz            | bim            |
| baz            | bim            |
| test test test | bim            |
| baz            | bim            |
| baz            | test test test |
| baz            | bim            |

: A long table. {tbl-colwidths="[50,50]"}

+-----------+--------------------+
| Fruit     | Advantages         |
+===========+====================+
| Bananas   | - built-in wrapper |
|           | - bright color     |
+-----------+--------------------+
| Oranges   | - cures scurvy     |
|           | - tasty            |
+-----------+--------------------+

: Sample grid table. {tbl-colwidths="[50,50]"}



+-----------+--------------------+
| Fruit     | Advantages         |
+===========+====================+
| Bananas   | - built-in wrapper |
|           | - bright color     |
+-----------+--------------------+
| Oranges   | - cures scurvy     |
|           | - tasty            |
+-----------+--------------------+

: Sample grid table. {tbl-colwidths="[50,50]"}

+:---------------------------------------:+:-----------------------------------------:+:------------------------------------------:+
| ![RAD](images/radiator.jpg){width=30mm} | ![RAD](images/radiator-2.jpg){width=30mm} |  ![RAD](images/radiator-3.jpg){width=30mm} |
+-----------------------------------------+-------------------------------------------+--------------------------------------------+

: Images in a table. {tbl-colwidths="[33,33,33]"}

+-----------+--------------------+
| Fruit     | Advantages         |
+===========+====================+
| Bananas   | - built-in wrapper |
|           | - bright color     |
+-----------+--------------------+
| Oranges   | - cures scurvy     |
|           | - tasty            |
+-----------+--------------------+
| Bananas   | - built-in wrapper |
|           | - bright color     |
+-----------+--------------------+
| Oranges   | - cures scurvy     |
|           | - tasty            |
+-----------+--------------------+
| Bananas   | - built-in wrapper |
|           | - bright color     |
+-----------+--------------------+
| Oranges   | - cures scurvy     |
|           | - tasty            |
+-----------+--------------------+
| Bananas   | - built-in wrapper |
|           | - bright color     |
+-----------+--------------------+
| Oranges   | - cures scurvy     |
|           | - tasty            |
+-----------+--------------------+
| Bananas   | - built-in wrapper |
|           | - bright color     |
+-----------+--------------------+
| Oranges   | - cures scurvy     |
|           | - tasty            |
+-----------+--------------------+
| Bananas   | - built-in wrapper |
|           | - bright color     |
+-----------+--------------------+
| Oranges   | - cures scurvy     |
|           | - tasty            |
+-----------+--------------------+
| Bananas   | - built-in wrapper |
|           | - bright color     |
+-----------+--------------------+
| Oranges   | - cures scurvy     |
|           | - tasty            |
+-----------+--------------------+
| Bananas   | - built-in wrapper |
|           | - bright color     |
+-----------+--------------------+
| Oranges   | - cures scurvy     |
|           | - tasty            |
+-----------+--------------------+
| Bananas   | - built-in wrapper |
|           | - bright color     |
+-----------+--------------------+
| Oranges   | - cures scurvy     |
|           | - tasty            |
+-----------+--------------------+
| Bananas   | - built-in wrapper |
|           | - bright color     |
+-----------+--------------------+
| Oranges   | - cures scurvy     |
|           | - tasty            |
+-----------+--------------------+
| Bananas   | - built-in wrapper |
|           | - bright color     |
+-----------+--------------------+
| Oranges   | - cures scurvy     |
|           | - tasty            |
+-----------+--------------------+

: A long grid table. {tbl-colwidths="[50,50]"}
