# EndingsCg

Simple endings cg gallery on RenPy 

## How to use

**Attention!!!**
This module uses persistent data, so after any change you must clear persistent data.

To integrate in your project:

* Copy the **screens.rpy, allEndings.rpy, endingsCgImpl.rpy** files in your project folder
* In the **allEndings.rpy** file Define your endings cg  comment 

```python
init offset = 1
init python:
    myEndingCg = endingCg("Fast ending", "endigFast.jpg")
    ...
```

## Usage

in script use $yourEndingst.open()

Example:
```python
label start:
    scene sc scene1
	"Bla bla blah bla blah"
    ...
    jump fastEnding
    
label fastEnding:
	"Blah blah bla bla bla bla blah bla"
	"Blah  bla bla bla blah bla bla!"
	$myEndingCg.open()
```

-------------------------------------------------------------------------------

# In russian / на русском

Простейшая галерея концовок для RenPy

## Как добавить

**Внимание!!!**
Используются persistent(сохроняются даже после изменения набора концовок в файле), не забывайте очищать постоянные.

* Скопируй **screens.rpy, allEndings.rpy, endingsCgImpl.rpy** файлы в папку проекта
* В **allEndings.rpy** запиши свои cg

```python
init offset = 1
init python:
    myEndingCg = endingCg("Быстрая концовка", "endigFast.jpg")
    ...
```

## Использование

В script используй $yourEndingst.open()

Пример:
```python
label start:
    scene sc scene1
	"Бла бла блаа бла блаа"
    ...
    jump fastEnding
    
label fastEnding:
	"Блаа блаа бла бла бла бла блаа бла"
	"Блаа  бла бла бла блаа бла бла!"
	$myEndingCg.open()
```