# installing

```python
pip install tkinter
```

# import

```python
   import tkinter > everthing
   import tkinter as tk > alias
   from tkinter import ttk > new themed widgets
```

# Window

-   ### window / root = tk()
-   ### title > window name
-   ### geometry > size
-   ### config > more properties (background etc)
-   ### mainloop > continous execution

# Geometry Managers

> Tkinter uses the geometry manager to arrange widgets on a window or frame. Tkinter supports three geometry managers:

## 1. Pack

## 2. Grid

## 3. Place

# 1. Pack

> You use the pack geometry manager to arrange widgets in one direction, either vertically or horizontally.
> The pack geometry manager has many options:

## Side (df=top, bottom, left, right)

    > The side parameter determines the direction of the widgets in the layout

## Expand (true, false)

    > The expand determines whether the widget should expand to occupy any extra spaces allocated to the container.

## Fill (def=none, x, y, both)

    > The fill determines if a widget will occupy the available space.

## ipadx, ipady (value)

    > The ipadx and ipady parameters create internal paddings for widgets

## padx, pady (value)

    > The padx and pady parameters allow you to specify padding to be added horizontally and vertically.

## Anchor (e, w, n, s, ne, nw, se, sw, center)

    > The anchor parameter allows you to anchor the widget to the edge of the allocated space.

# 2. Grid

> The grid geometry manager uses the concepts of rows and columns to arrange the widgets on a window or frame.

## Setup Grid

```python tkinter
container.columnconfigure(index, weight)
container.rowconfigure(index, weight)
```

## Widget positioning

```python
widget.grid(column, row, sticky, padx, pady, ipadx, ipady)
```

# 3. Place

> The Tkinter place geometry manager allows you to specify the exact placement of a widget using either absolution or relative positioning.

```python tkinter
place(relx=0.5, rely=0.5, width=100, height=50, anchor=tk.CENTER)
```

## Positioning

### 1. Absolute (x,y)

```python tkinter
widget.place(x=50, y=50)
```

### 2. Relative (relx, rely)

```python tkinter
widget.place(relx=0.5, rely=0.5)
```

## Width , Height and Anchor

```python tkinter
widget.place(width=100, height=20, anchor=tk.N)
```
