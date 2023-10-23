```{toctree}
:maxdepth: 2
:caption: Contents

organize
share
definitions
online
```


<style>
  code {
    background: #e6ecdf;
    color:#000000;
  }

  pre {
    background:#cfdde2;
    color:#000000;
  }

    pre code {
    background: #e6ecdf;
    display: block;
    color:#000000;
  }
</style>

<style type="text/css">
  table    { background:#dce8ef; color: #000000; }
</style>

# [**rivt**](#definitions)

**rivt** is a markdown language for writing, organizing and sharing 
engineering documents. It emphasizes clarity, efficiency and access.

[rivtlib](https://rivt-code.net) is a Python library for processing rivt files.  It outputs formatted documents in a serveral different
formats. The minimum software needed to write rivt documents is Python 3.8
with Python science libraries, including **rivtlib**.

[rivt-doc](/organize.md) is an editing and publishing framework for rivt
using additional open source programs. **rivt** works
with single files, and with extensive reports using hundreds of files. 

<hr>

## Files
<hr>

A **rivt** file is a utf-8 Python file that includes the import statement
<code>import rivtlib.rivtapi as rv</code> which exposes four API functions.
Each function takes a triple quoted string as argument, which may include
arbitrary text.

<pre>
============= ========== =================================
API function   name           purpose
============= ========== =================================
rv.R(str)      rivtinit    repository and report settings
rv.I(str)      insert      static text, images and tables
rv.V(str)      values      equations
rv.T(str)      tools       Python functions and scripts
</pre>

When running in an IDE (e.g. VSCode) the file may be executed interactively.
Interactive output is formatted as utf-8 text for speed and compatiblility. API
functions may be grouped and executed step-wise using the standard cell decorator <code># %%</code>. Document and report files are generated by the functions <code>
rv.writemd()</code> and <code> rv.writepdf()</code> which write output files in GitHub Flavored Markdown
(GFM) and PDF formats respectively.

<hr>

## API Functions
<hr>

Each API function defines a document section. The first line of each function
includes a section label that converts to a section title, followed by section
formatting parameters. The titles and section breaks may be suppressed by
prepending a double hyphen.

The section body can contain any utf-8 text. Commands and tags applicable to
each function are defined [here](#commands) and
[here](#tags)


<pre>
============ ========================================================
  name                   API function definition
============ ========================================================

rivtinit      rv.R("""label | toc; notoc, start page

                  rivt settings, and text to be formatted and output to the
                  terminal.

                """)

insert        rv.I("""label | background color  

                  Static tables, images and text that are formmatted and output
                  to the terminal.

                """)

values        rv.V("""label | sub; nosub 

                  Equations and text that are evaluated, formatted and output
                  to the terminal.
                
                """)

tools         rv.T("""label | line; noline | print; noprint

                  Python code evaluated in the rivt namespace.

                """)

exclude       rv.X("""any text

                  Any function changed to X is not processed. Used for
                  comments and debugging.

                """)

write-md      rv.writemd()
        
              Writes a markdown document file (default is a GitHub README.md)

write-pdf     rv.writepdf()
    
              Writes a markdown (default is a GitHub README.md) 
              and PDF document file (default uses rivt file name.)

all-readme    rv.readme()

              Collects, in order, all README.md document files in the project
              and writes them into a single README.md in the root project
              folder, making the project full-text searchable on GitHub. Note
              that file links in the document README will typically not resolve
              when compiled into the project README. This is by design. It
              makes the full-project README faster to search. For convenience
              links are inserted back to the original document README.
          
</pre>

The API function names start in column one. All other content is indented 4
spaces to facilitate section folding, bookmarking and legibility. API functions
can be written in any order and frequency except for *rivtinit*, which occurs
only once as the initial function in the file. A **rivt** file is a Python file
that follows pep8 and ruff conventions.

<hr>


# **Syntax**

**rivt** markup uses a syntax of commands for file operations and tags for text
formatting. Any text not defined with commands or tags is passed through as
output. Commands and tags are processed in part by the *docutils* library and 
[restructuredText](https://docutils.sourceforge.io/docs/user/rst/quickref.html).


<hr>

## Commands
<hr>

Commands read and write external files and are marked by double bars (||) at
the beginning of a line. Command parameters are separated by a single bar (|).
In the summary below parameter options are separated with semi-colons,
parameter list elements are separated with commas, and options are in
parenthesis.

File locations are specified using shortene, relative paths that include the
name of the file and the name of its containing folder. Folder organization is
described [here](/organize.md#folders)


```{list-table}
:header-rows: 1

* - command 
  - API 
* - || [text](#text) | relative path | rivt; plain                     
  - R I V
* - || [init](#init) | relative path
  - R
* - || [append](#append) | relative path | cover.pdf
  - R
* - || [image](#image)  | relative path, (2nd path) | width, (width)
  - I
* - || [table](#table)  | relative path | max col width, align
  - I
* - || [declare](#declare) | relative path |  print; noprint
  - V
```


### **text**

The text command inserts and formats text from external files. Text files may
be plain text or text with rivt tags.

### **init**

The init command specifies the name of the configuration file which is read
from the rivt-doc folder. Report formatting can be easily modified by
specifying a different init file.

### **append**

The append command attaches PDF files to the end of the doc.

### **image**

The image command inserts and formats image data from png or jpg files.

### **table**

The table command inserts and formats tabular data from csv or xls files.

### **declare**

The declare command imports values from a csv file written by rivt when
processing assigned and declared values from another doc in the same
project.



<hr>

## Tags
<hr>

Line tags format a line of text and are denoted with *_[tag]*, typically at the
end of a line. The *=* and *:=* tags used in the Value method are unique
exceptions. 

```{list-table} 
:header-rows: 1

* - line tags
  - description
  - API
* - text _[b]
  - bold
  - R I V 
* - text _[c]
  - center
  - R I V  
* - text _[i]
  - italic
  - R I V  
* - text _[bc]
  - bold-center
  - R I V  
* - text _[bi]
  - bold-italic
  - R I V
* - text _[r]
  - right justify
  - R I V
* - text _[u]
  - underline
  - R I V   
* - text _[l]
  - LaTeX math
  - I V
* - text _[s]
  - sympy math
  - I V
* - text _[bs]
  - bold-sympy math
  - I V
* - text _[e]
  - equation label, autonumber
  - I V
* - text _[f]
  - figure caption, autonumber
  - I V
* - text _[t]
  - table title, autonumber
  - I V
* - text _[#]
  - footnote, autonumber
  - I V
* - text _[d]
  - footnote description
  - I V
* - _[page]
  - new page
  - I V
* - _[address, label]
  - url or internal reference
  - I V
* - a = 1.2 | unit, alt | descrip
  - declare =
  - V
* - a := b + c | unit, alt | n,n
  - assign :=
  - V
```

Block tags start a text block with *_[[tag]]* and end with *_[[q]]*.

```{list-table} 
:header-rows: 1

* - block tags
  - description
  - API

* - _[[b]]
  - bold
  - R I V

* - _[[c]]
  - center
  - R I V

* - _[[i]]
  - italic
  - R I V

* - _[[p]]
  - plain
  - R I V

* - _[[q]]
  - quit block
  - R I V

* - _[[l]]
  - LaTeX
  - I V
```

# **Examples**

<hr>

## Simple
<hr>

```{code-block}
:linenos:

import rivtlib.rivtapi as rv

rv.R("""Introduction | notoc, 1

    The Repo method (short for repository and report) is the first method of a
    rivt file which specifies document configuration settings.

    The first line of any method is the heading line, which starts a new
    document section. If the section heading is preceded by two dashes (--) it
    becomes a section reference and a new section is not started. The toc
    parameter specifies whether a document table of contents is generated (not
    to be confused with a report table of contents). The page number is the
    starting page number for the doc when processed as a stand alone document.

    The init command specifies the name of the configuration file which is read
    from the rivt-doc folder. Report formatting can be easily modified by
    specifying a different init file.

    ||init | rivt01.ini

    The text command inserts text from an external file. Text files may be
    plain text or include rivt tags.

    ||text | private/text/proj.txt | plain
    
    The append command attaches PDF files to the end of the doc.

    || append | append/report1.pdf
    || append | append/report2.pdf

    """)

rv.I("""The Insert method | default 

    The Insert method formats static information e.g. images and text. The
    color command specifies a background color for the section.

    The text command inserts and formats text from external files into the
    rivt file. Text files may be plain text or text with rivt tags.

    ||text | data0101/describe.txt | rivt     

    The table command inserts and formats tabular data from csv or xls files.
    
    The _[t] tag formats and autonumbers table titles.

    A table title  _[t]
    || table | data0101/file.csv | 60,r

    The image command inserts and formats image data from png or jpg files.

    The _[f] tag formats and autonumbers figures.
        
    A figure caption _[f]
    || image | data0101/f1.png | 50

    Two images may be placed side by side as follows:

    The first figure caption  _[f]
    The second figure caption  _[f]
    || image | private/image/f2.png, private/image/f3.png | 45,35
    
    The tags _[x] and _[s] format LaTeX and sympy equations:

    \gamma = \frac{5}{x+y} + 3  _[x] 

    x = 32 + (y/2)  _[s]

    """)

rv.V("""The Values method |  sub; nosub 

    The Values method assigns values to variables and evaluates equations. The
    sub; nosub setting specifies whether the equations are printed a second
    time with substituted numerical values.

    A table tag provides a table title and number.  
    
    The equal tag declares a value. A sequence of declared values terminated
    with a blank line are formatted as a table.
    
    Example of assignment list _[t]
    f1 = 10.1 * LBF | N | a force
    d1 = 12.1 * IN | CM | a length

    An equation tag provides an equation description and number. A colon-equal
    tag assigns a value and specifies the result units and printed output
    decimal places in the result and equation.

    Example equation - Area of circle  _[e]
    a1 := 3.14(d1/2)^2 | IN^2, CM^2 | 1,2

    || declare | data0102/values0102.csv
    
    The declare command imports values from a csv file written by rivt when
    processing assigned and declared values from another doc in the same
    project.

    """)
```


### text output

<pre style="background: #cfdde2; color: #000000">

import rivt.rivtapi as rv

rv.R("""Introduction | notoc, 1

    The Repo method (short for repository and report) is the first method of a
    rivt file which specifies document configuration settings.

    The first line of any method is the heading line, which starts a new
    document section. If the section heading is preceded by two dashes (--) it
    becomes a section reference and a new section is not started. The toc
    parameter specifies whether a document table of contents is generated (not
    to be confused with a report table of contents). The page number is the
    starting page number for the doc when processed as a stand alone document.

    The init command specifies the name of the configuration file which is read
    from the rivt-doc folder. Report formatting can be easily modified by
    specifying a different init file.

    ||init | rivt01.ini

    The text command inserts text from an external file. Text files may be
    plain text or include rivt tags.

    ||text | private/text/proj.txt | plain
    
    The append command attaches PDF files to the end of the doc.

    || append | append/report1.pdf
    || append | append/report2.pdf

    
    """)

rv.I("""The Insert method | default 

    The Insert method formats static information e.g. images and text. The
    color command specifies a background color for the section.

    The text command inserts and formats text from external files into the
    rivt file. Text files may be plain text or text with rivt tags.

    ||text | data0101/describe.txt | rivt     

    The table command inserts and formats tabular data from csv or xls files.
    
    The _[t] tag formats and autonumbers table titles.

    A table title  _[t]
    || table | data0101/file.csv | 60,r

    The image command inserts and formats image data from png or jpg files.

    The _[f] tag formats and autonumbers figures.
        
    A figure caption _[f]
    || image | data0101/f1.png | 50

    Two images may be placed side by side as follows:

    The first figure caption  _[f]
    The second figure caption  _[f]
    || image | private/image/f2.png, private/image/f3.png | 45,35
    
    The tags _[x] and _[s] format LaTeX and sympy equations:

    \gamma = \frac{5}{x+y} + 3  _[x] 

    x = 32 + (y/2)  _[s]

    """)

rv.V("""The Values method |  sub; nosub 

    The Values method assigns values to variables and evaluates equations. The
    sub; nosub setting specifies whether the equations are printed a second
    time with substituted numerical values.

    A table tag provides a table title and number.  
    
    The equal tag declares a value. A sequence of declared values terminated
    with a blank line are formatted as a table.
    
    Example of assignment list _[t]
    f1 = 10.1 * LBF | N | a force
    d1 = 12.1 * IN | CM | a length

    An equation tag provides an equation description and number. A colon-equal
    tag assigns a value and specifies the result units and printed output
    decimal places in the result and equation.

    Example equation - Area of circle  _[e]
    a1 := 3.14(d1/2)^2 | IN^2, CM^2 | 1,2

    || declare | data0102/values0102.csv
    
    The declare command imports values from a csv file written by rivt when
    processing assigned and declared values from another doc in the same
    project.

    """)

rv.T("""The Tools method | color 

    # The Tools method processes Python code in the rivt namespace and prints
    # the code and result of any print statement in the doc. New functions 
    # may be written explicitly or imported from other files. Line comments 
    # are printed. Triple quotes cannot be used. Use raw strings instead.
    
    # Four Python libraries, if installed, are imported by rivt and available as: 
    # pyplot -> plt
    # numpy -> np
    # pandas -> pd
    # sympy -> sy
    
    # Python code:
    
    def f1(x,y): z = x + y
        print(z)
        return Z

    with open('file.csv', 'r') as f: 
        input = f.readlines()
    
    var = range(10)
    with open('fileout.csv', 'w') as f: 
        f.write(var)
        
    """)

rv.X("""any text

    Changing a function to X skips evaluation of that function and may be used
    for review comments and debugging.

    """) 
</pre>


### markdown output

some markdown


### PDF output

[PDF output from example](./_static/attach/rivt-toy-example.pdf)

<hr>

## Solar Canopy
<hr>
xyz

### text output

ccc

<hr>

## Seismic Strengthening
<hr>

xyz

### text output

ccc