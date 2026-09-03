# City Skyline — solución paso a paso

Los 115 pasos de *Learn CSS Variables by Building a City Skyline* (freeCodeCamp).
Para cada paso verás el cambio exacto que hay que hacer. El código completo de
cada paso está en `pasos/paso-NNN/` (`styles.css` e `index.html`), listo para copiar.

Los enunciados están en inglés porque así vienen en el código fuente del curso;
en tu plataforma los verás traducidos.

## Paso 1

> Welcome to the CSS Variables Skyline project! Start by adding a `link` element that links your `styles.css` file within the `head` element.

Cambio en `index.html`:

```diff
@@ -3,7 +3,7 @@
   <head>
     <meta charset="UTF-8">
     <title>City Skyline</title>
-
+    <link href="styles.css" rel="stylesheet" />
   </head>
 
   <body>
```

Código completo tras este paso: `pasos/paso-001/`

## Paso 2

> In CSS, you can target everything with an asterisk. Add a border to everything by using the `*` selector, and giving it a `border` of `1px solid black`. This is a trick that helps visualize where elements are and their size. You will remove this later.

Cambio en `styles.css`:

```diff
@@ -1,2 +1,5 @@
+* {
+  border: 1px solid black;
 
+}
 
```

Código completo tras este paso: `pasos/paso-002/`

## Paso 3

> Also add a `box-sizing` of `border-box` to everything. This will make it so the border you added doesn't add any size to your elements.

Cambio en `styles.css`:

```diff
@@ -1,5 +1,5 @@
 * {
   border: 1px solid black;
-
+  box-sizing: border-box;
 }
 
```

Código completo tras este paso: `pasos/paso-003/`

## Paso 4

> You can see the `body` (it's the inner-most box on your page); the box around it is the `html` element. Make your `body` fill the whole viewport by giving it a `height` of `100vh`. Remove the default `margin` from the `body` by setting the `margin` to `0`. Finally, set the `overflow` property to `hidden` to hide any scroll bars that appear when something extends past the viewport.

Cambio en `index.html`:

```diff
@@ -7,6 +7,7 @@
   </head>
 
   <body>
+
   </body>
 </html>
 
```

Cambio en `styles.css`:

```diff
@@ -3,3 +3,9 @@
   box-sizing: border-box;
 }
 
+body {
+  height: 100vh;
+  margin: 0;
+  overflow: hidden;
+}
+
```

Código completo tras este paso: `pasos/paso-004/`

## Paso 5

> Create a `div` element in the `body` with a class of `background-buildings`. This will be a container for a group of buildings.

Cambio en `index.html`:

```diff
@@ -7,7 +7,7 @@
   </head>
 
   <body>
-
+    <div class="background-buildings"></div>
   </body>
 </html>
 
```

Código completo tras este paso: `pasos/paso-005/`

## Paso 6

> Give your `.background-buildings` element a `width` and `height` of `100%` to make it the full width and height of its parent, the `body`.

Cambio en `index.html`:

```diff
@@ -7,7 +7,9 @@
   </head>
 
   <body>
-    <div class="background-buildings"></div>
+    <div class="background-buildings">
+
+    </div>
   </body>
 </html>
 
```

Cambio en `styles.css`:

```diff
@@ -9,3 +9,8 @@
   overflow: hidden;
 }
 
+.background-buildings {
+  width: 100%;
+  height: 100%;
+}
+
```

Código completo tras este paso: `pasos/paso-006/`

## Paso 7

> Nest a `div` with a class of `bb1` in the background buildings container. Open your `styles.css` file, and give `.bb1` a `width` of `10%` and `height` of `70%`. "bb" stands for "background building", this will be your first building.

Cambio en `index.html`:

```diff
@@ -8,7 +8,9 @@
 
   <body>
     <div class="background-buildings">
+      <div class="bb1">
 
+      </div>
     </div>
   </body>
 </html>
```

Cambio en `styles.css`:

```diff
@@ -14,3 +14,8 @@
   height: 100%;
 }
 
+.bb1 {
+  width: 10%;
+  height: 70%;
+}
+
```

Código completo tras este paso: `pasos/paso-007/`

## Paso 8

> Nest four `div` elements in the `.bb1` container. Give them the classes `bb1a`, `bb1b`, `bb1c`, and `bb1d` in that order. This building will have four sections.

Cambio en `index.html`:

```diff
@@ -9,7 +9,10 @@
   <body>
     <div class="background-buildings">
       <div class="bb1">
-
+        <div class="bb1a"></div>
+        <div class="bb1b"></div>
+        <div class="bb1c"></div>
+        <div class="bb1d"></div>
       </div>
     </div>
   </body>
```

Código completo tras este paso: `pasos/paso-008/`

## Paso 9

> Give the parts of your building `width` and `height` properties with these values: `70%` and `10%` to `.bb1a`, `80%` and `10%` to `.bb1b`, `90%` and `10%` to `.bb1c`, and `100%` and `70%` to `.bb1d`. Remember that these percentages are relative to the parent and note that the heights will add up to 100% - vertically filling the container.

Cambio en `styles.css`:

```diff
@@ -17,5 +17,26 @@
 .bb1 {
   width: 10%;
   height: 70%;
+
 }
 
+.bb1a {
+  width: 70%;
+  height: 10%;
+}
+
+.bb1b {
+  width: 80%;
+  height: 10%;
+}
+
+.bb1c {
+  width: 90%;
+  height: 10%;
+}
+
+.bb1d {
+  width: 100%;
+  height: 70%;
+}
+
```

Código completo tras este paso: `pasos/paso-009/`

## Paso 10

> Center the parts of your building by turning the `.bb1` element into a flexbox parent. Use the `flex-direction` and `align-items` properties to center the children.

Cambio en `styles.css`:

```diff
@@ -17,6 +17,9 @@
 .bb1 {
   width: 10%;
   height: 70%;
+  display: flex;
+  flex-direction: column;
+  align-items: center;
 
 }
 
```

Código completo tras este paso: `pasos/paso-010/`

## Paso 11

> Now you have something that is resembling a building. You are ready to create your first variable. In previous lessons you learned that variable declarations begin with two dashes (`-`) and are given a name and a value like this: `--variable-name: value;`. In the rule for the `bb1` class, create a variable named `--building-color1` and give it a value of `#999`.

Cambio en `styles.css`:

```diff
@@ -20,12 +20,13 @@
   display: flex;
   flex-direction: column;
   align-items: center;
-
+  --building-color1: #999;
 }
 
 .bb1a {
   width: 70%;
   height: 10%;
+
 }
 
 .bb1b {
```

Código completo tras este paso: `pasos/paso-011/`

## Paso 12

> To use a variable, put the variable name in parentheses with `var` in front of them like this: `var(--variable-name)`. Whatever value you gave the variable will be applied to whatever property you use it on. 
> 
> Add the variable `--building-color1` you created in the previous step as the value of the `background-color` property of the `.bb1a` class.

Cambio en `styles.css`:

```diff
@@ -26,21 +26,24 @@
 .bb1a {
   width: 70%;
   height: 10%;
-
+  background-color: var(--building-color1);
 }
 
 .bb1b {
   width: 80%;
   height: 10%;
+
 }
 
 .bb1c {
   width: 90%;
   height: 10%;
+
 }
 
 .bb1d {
   width: 100%;
   height: 70%;
+
 }
 
```

Código completo tras este paso: `pasos/paso-012/`

## Paso 13

> Use the same variable as the `background-color` of the `.bb1b`, `.bb1c`, and `.bb1d` classes to fill in the rest of the building.

Cambio en `styles.css`:

```diff
@@ -32,18 +32,18 @@
 .bb1b {
   width: 80%;
   height: 10%;
-
+  background-color: var(--building-color1);
 }
 
 .bb1c {
   width: 90%;
   height: 10%;
-
+  background-color: var(--building-color1);
 }
 
 .bb1d {
   width: 100%;
   height: 70%;
-
+  background-color: var(--building-color1);
 }
 
```

Código completo tras este paso: `pasos/paso-013/`

## Paso 14

> Change the value of your variable from `#999` to `#aa80ff` and you can see how it gets applied everywhere you used the variable. This is the main advantage of using variables, being able to quickly change many values in your stylesheet by just changing the value of a variable.

Cambio en `index.html`:

```diff
@@ -14,6 +14,7 @@
         <div class="bb1c"></div>
         <div class="bb1d"></div>
       </div>
+
     </div>
   </body>
 </html>
```

Cambio en `styles.css`:

```diff
@@ -20,7 +20,7 @@
   display: flex;
   flex-direction: column;
   align-items: center;
-  --building-color1: #999;
+  --building-color1: #aa80ff;
 }
 
 .bb1a {
```

Código completo tras este paso: `pasos/paso-014/`

## Paso 15

> Your first building looks pretty good now. Nest three new `div` elements in the `.background-buildings` container and give them the classes of `bb2`, `bb3`, and `bb4` in that order. These will be three more buildings for the background.

Cambio en `index.html`:

```diff
@@ -14,7 +14,9 @@
         <div class="bb1c"></div>
         <div class="bb1d"></div>
       </div>
-
+      <div class="bb2"></div>
+      <div class="bb3"></div>
+      <div class="bb4"></div>
     </div>
   </body>
 </html>
```

Código completo tras este paso: `pasos/paso-015/`

## Paso 16

> Give the new buildings `width` and `height` properties of: `10%` and `50%` for `.bb2`, `10%` and `55%` for `.bb3`, and `11%` and `58%` for `.bb4`. You will be using almost all percent based units and some flexbox for this project, so everything will be completely responsive.

Cambio en `styles.css`:

```diff
@@ -12,6 +12,7 @@
 .background-buildings {
   width: 100%;
   height: 100%;
+
 }
 
 .bb1 {
@@ -47,3 +48,18 @@
   background-color: var(--building-color1);
 }
 
+.bb2 {
+  width: 10%;
+  height: 50%;
+}
+
+.bb3 {
+  width: 10%;
+  height: 55%;
+}
+
+.bb4 {
+  width: 11%;
+  height: 58%;
+}
+
```

Código completo tras este paso: `pasos/paso-016/`

## Paso 17

> The buildings are currently stacked on top of each other. Align the buildings by turning the `.background-buildings` element into a flexbox parent. Use the `align-items` and `justify-content` properties to evenly space the buildings across the bottom of the element.

Cambio en `index.html`:

```diff
@@ -8,6 +8,7 @@
 
   <body>
     <div class="background-buildings">
+
       <div class="bb1">
         <div class="bb1a"></div>
         <div class="bb1b"></div>
@@ -16,7 +17,9 @@
       </div>
       <div class="bb2"></div>
       <div class="bb3"></div>
+
       <div class="bb4"></div>
+
     </div>
   </body>
 </html>
```

Cambio en `styles.css`:

```diff
@@ -12,7 +12,9 @@
 .background-buildings {
   width: 100%;
   height: 100%;
-
+  display: flex;
+  align-items: flex-end;
+  justify-content: space-evenly;
 }
 
 .bb1 {
```

Código completo tras este paso: `pasos/paso-017/`

## Paso 18

> The buildings are too spaced out. Squeeze them together by adding two empty `div` elements to the top of the `.background-buildings` element, two more at the bottom of it, and one more in between `.bb3` and `.bb4`. These will be added as evenly-spaced elements across the container, effectively moving the buildings closer to the center.

Cambio en `index.html`:

```diff
@@ -8,7 +8,8 @@
 
   <body>
     <div class="background-buildings">
-
+      <div></div>
+      <div></div>
       <div class="bb1">
         <div class="bb1a"></div>
         <div class="bb1b"></div>
@@ -17,9 +18,10 @@
       </div>
       <div class="bb2"></div>
       <div class="bb3"></div>
-
+      <div></div>
       <div class="bb4"></div>
-
+      <div></div>
+      <div></div>
     </div>
   </body>
 </html>
```

Cambio en `styles.css`:

```diff
@@ -24,6 +24,7 @@
   flex-direction: column;
   align-items: center;
   --building-color1: #aa80ff;
+
 }
 
 .bb1a {
@@ -53,6 +54,7 @@
 .bb2 {
   width: 10%;
   height: 50%;
+
 }
 
 .bb3 {
```

Código completo tras este paso: `pasos/paso-018/`

## Paso 19

> Create a new variable below your `--building-color1` variable. Name your new variable `--building-color2` and give it a value of `#66cc99`. Then set it as the `background-color` of `.bb2`.

Cambio en `styles.css`:

```diff
@@ -24,7 +24,7 @@
   flex-direction: column;
   align-items: center;
   --building-color1: #aa80ff;
-
+  --building-color2: #66cc99;
 }
 
 .bb1a {
@@ -54,7 +54,7 @@
 .bb2 {
   width: 10%;
   height: 50%;
-
+  background-color: var(--building-color2);
 }
 
 .bb3 {
```

Código completo tras este paso: `pasos/paso-019/`

## Paso 20

> That didn't work. You should add a fallback value to a variable by putting it as the second value of where you use the variable like this: `var(--variable-name, fallback-value)`. The property will use the fallback value when there's a problem with the variable. Add a fallback value of `green` to the `background-color` of `.bb2`.

Cambio en `styles.css`:

```diff
@@ -25,6 +25,7 @@
   align-items: center;
   --building-color1: #aa80ff;
   --building-color2: #66cc99;
+
 }
 
 .bb1a {
@@ -54,12 +55,13 @@
 .bb2 {
   width: 10%;
   height: 50%;
-  background-color: var(--building-color2);
+  background-color: var(--building-color2, green);
 }
 
 .bb3 {
   width: 10%;
   height: 55%;
+
 }
 
 .bb4 {
```

Código completo tras este paso: `pasos/paso-020/`

## Paso 21

> Create a new variable below the other ones named `--building-color3` and give it a value of `#cc6699`. Then use it as the `background-color` of the `.bb3` class and give it a fallback value of `pink`.

Cambio en `styles.css`:

```diff
@@ -1,3 +1,5 @@
+
+
 * {
   border: 1px solid black;
   box-sizing: border-box;
@@ -25,7 +27,7 @@
   align-items: center;
   --building-color1: #aa80ff;
   --building-color2: #66cc99;
-
+  --building-color3: #cc6699;
 }
 
 .bb1a {
@@ -61,7 +63,7 @@
 .bb3 {
   width: 10%;
   height: 55%;
-
+  background-color: var(--building-color3, pink);
 }
 
 .bb4 {
```

Código completo tras este paso: `pasos/paso-021/`

## Paso 22

> That didn't work, because the variables you declared in `.bb1` do not cascade to the `.bb2` and `.bb3` sibling elements. That's just how CSS works. Because of this, variables are often declared in the `:root` selector. This is the highest level selector in CSS; putting your variables there will make them usable everywhere. Add the `:root` selector to the top of your stylesheet, and move all your variable declarations there.

Cambio en `styles.css`:

```diff
@@ -1,4 +1,8 @@
-
+:root {
+  --building-color1: #aa80ff;
+  --building-color2: #66cc99;
+  --building-color3: #cc6699;
+}
 
 * {
   border: 1px solid black;
@@ -25,9 +29,6 @@
   display: flex;
   flex-direction: column;
   align-items: center;
-  --building-color1: #aa80ff;
-  --building-color2: #66cc99;
-  --building-color3: #cc6699;
 }
 
 .bb1a {
```

Código completo tras este paso: `pasos/paso-022/`

## Paso 23

> Now that you've worked the bugs out and the buildings are the right colors, you can remove the fallback values in the two places they were used. Go ahead and do that now.

Cambio en `styles.css`:

```diff
@@ -2,6 +2,7 @@
   --building-color1: #aa80ff;
   --building-color2: #66cc99;
   --building-color3: #cc6699;
+
 }
 
 * {
@@ -58,17 +59,18 @@
 .bb2 {
   width: 10%;
   height: 50%;
-  background-color: var(--building-color2, green);
+  background-color: var(--building-color2);
 }
 
 .bb3 {
   width: 10%;
   height: 55%;
-  background-color: var(--building-color3, pink);
+  background-color: var(--building-color3);
 }
 
 .bb4 {
   width: 11%;
   height: 58%;
+
 }
 
```

Código completo tras este paso: `pasos/paso-023/`

## Paso 24

> Create another variable named `--building-color4` and give it a value of `#538cc6`. Make sure it's in the `:root` selector this time. Then use it to fill in the last building.

Cambio en `index.html`:

```diff
@@ -23,6 +23,8 @@
       <div></div>
       <div></div>
     </div>
+
+
   </body>
 </html>
 
```

Cambio en `styles.css`:

```diff
@@ -2,7 +2,7 @@
   --building-color1: #aa80ff;
   --building-color2: #66cc99;
   --building-color3: #cc6699;
-
+  --building-color4: #538cc6;
 }
 
 * {
@@ -71,6 +71,6 @@
 .bb4 {
   width: 11%;
   height: 58%;
-
+  background-color: var(--building-color4);
 }
 
```

Código completo tras este paso: `pasos/paso-024/`

## Paso 25

> The background buildings are starting to look pretty good. Create a new `div` below the `.background-buildings` element and give it a class of `foreground-buildings`. This will be another container for more buildings.

Cambio en `index.html`:

```diff
@@ -24,7 +24,7 @@
       <div></div>
     </div>
 
-
+    <div class="foreground-buildings"></div>
   </body>
 </html>
 
```

Código completo tras este paso: `pasos/paso-025/`

## Paso 26

> You want the `.foreground-buildings` container to sit directly on top of the `.background-buildings` element. Give it a `width` and `height` of `100%`, set the `position` to `absolute`, and the `top` to `0`. This will make it the same size as the body and move the start of it to the top left corner.

Cambio en `index.html`:

```diff
@@ -24,7 +24,9 @@
       <div></div>
     </div>
 
-    <div class="foreground-buildings"></div>
+    <div class="foreground-buildings">
+
+    </div>
   </body>
 </html>
 
```

Cambio en `styles.css`:

```diff
@@ -74,3 +74,10 @@
   background-color: var(--building-color4);
 }
 
+.foreground-buildings {
+  width: 100%;
+  height: 100%;
+  position: absolute;
+  top: 0;
+}
+
```

Código completo tras este paso: `pasos/paso-026/`

## Paso 27

> Nest six `div` elements within `.foreground-buildings` and give them the classes of `fb1` through `fb6` in that order. "fb" stands for "foreground building". These will be six more buildings for the foreground.

Cambio en `index.html`:

```diff
@@ -25,7 +25,12 @@
     </div>
 
     <div class="foreground-buildings">
-
+      <div class="fb1"></div>
+      <div class="fb2"></div>
+      <div class="fb3"></div>
+      <div class="fb4"></div>
+      <div class="fb5"></div>
+      <div class="fb6"></div>
     </div>
   </body>
 </html>
```

Código completo tras este paso: `pasos/paso-027/`

## Paso 28

> Give the six new elements these `width` and `height` values: `10%` and `60%` to `.fb1`, `10%` and `40%` to `.fb2`, `10%` and `35%` to `.fb3`, `8%` and `45%` to `.fb4`, `10%` and `33%` to `.fb5`, and `9%` and `38%` to `.fb6`.

Cambio en `styles.css`:

```diff
@@ -79,5 +79,36 @@
   height: 100%;
   position: absolute;
   top: 0;
+
 }
 
+.fb1 {
+  width: 10%;
+  height: 60%;
+}
+
+.fb2 {
+  width: 10%;
+  height: 40%;
+}
+
+.fb3 {
+  width: 10%;
+  height: 35%;
+}
+
+.fb4 {
+  width: 8%;
+  height: 45%;
+}
+
+.fb5 {
+  width: 10%;
+  height: 33%;
+}
+
+.fb6 {
+  width: 9%;
+  height: 38%;
+}
+
```

Código completo tras este paso: `pasos/paso-028/`

## Paso 29

> Add the same `display`, `align-items`, and `justify-content` properties and values to `.foreground-buildings` that you used on `.background-buildings`. Again, this will use Flexbox to evenly space the buildings across the bottom of their container.

Cambio en `styles.css`:

```diff
@@ -79,7 +79,9 @@
   height: 100%;
   position: absolute;
   top: 0;
-
+  display: flex;
+  align-items: flex-end;
+  justify-content: space-evenly;
 }
 
 .fb1 {
```

Código completo tras este paso: `pasos/paso-029/`

## Paso 30

> You should optimize your code. Move the `position` and `top` properties and values from `.foreground-buildings` to `.background-buildings`. Then select both `.background-buildings` and `.foreground-buildings` there, effectively applying those styles to both of the elements. You can use a comma (`,`) to separate selectors like this: `selector1, selector2`.

Cambio en `styles.css`:

```diff
@@ -16,12 +16,14 @@
   overflow: hidden;
 }
 
-.background-buildings {
+.background-buildings, .foreground-buildings {
   width: 100%;
   height: 100%;
   display: flex;
   align-items: flex-end;
   justify-content: space-evenly;
+  position: absolute;
+  top: 0;
 }
 
 .bb1 {
@@ -77,8 +79,6 @@
 .foreground-buildings {
   width: 100%;
   height: 100%;
-  position: absolute;
-  top: 0;
   display: flex;
   align-items: flex-end;
   justify-content: space-evenly;
```

Código completo tras este paso: `pasos/paso-030/`

## Paso 31

> Now that you did that, you can delete the old `.foreground-buildings` declaration and all of its properties since they aren't needed anymore.

Cambio en `styles.css`:

```diff
@@ -76,41 +76,39 @@
   background-color: var(--building-color4);
 }
 
-.foreground-buildings {
-  width: 100%;
-  height: 100%;
-  display: flex;
-  align-items: flex-end;
-  justify-content: space-evenly;
-}
-
 .fb1 {
   width: 10%;
   height: 60%;
+
 }
 
 .fb2 {
   width: 10%;
   height: 40%;
+
 }
 
 .fb3 {
   width: 10%;
   height: 35%;
+
 }
 
 .fb4 {
   width: 8%;
   height: 45%;
+
 }
 
 .fb5 {
   width: 10%;
   height: 33%;
+
 }
 
 .fb6 {
   width: 9%;
   height: 38%;
+
 }
 
```

Código completo tras este paso: `pasos/paso-031/`

## Paso 32

> The skyline is coming together. Fill in the `background-color` property of the foreground buildings. Use your `--building-color1` variable to fill in `.fb3` and `.fb4`, `--building-color2` for `.fb5`, `--building-color3` for `.fb2` and `.fb6`, and `--building-color4` for `.fb1`.

Cambio en `index.html`:

```diff
@@ -25,12 +25,15 @@
     </div>
 
     <div class="foreground-buildings">
+
       <div class="fb1"></div>
       <div class="fb2"></div>
+
       <div class="fb3"></div>
       <div class="fb4"></div>
       <div class="fb5"></div>
       <div class="fb6"></div>
+
     </div>
   </body>
 </html>
```

Cambio en `styles.css`:

```diff
@@ -79,36 +79,36 @@
 .fb1 {
   width: 10%;
   height: 60%;
-
+  background-color: var(--building-color4);
 }
 
 .fb2 {
   width: 10%;
   height: 40%;
-
+  background-color: var(--building-color3);
 }
 
 .fb3 {
   width: 10%;
   height: 35%;
-
+  background-color: var(--building-color1);
 }
 
 .fb4 {
   width: 8%;
   height: 45%;
-
+  background-color: var(--building-color1);
 }
 
 .fb5 {
   width: 10%;
   height: 33%;
-
+  background-color: var(--building-color2);
 }
 
 .fb6 {
   width: 9%;
   height: 38%;
-
+  background-color: var(--building-color3);
 }
 
```

Código completo tras este paso: `pasos/paso-032/`

## Paso 33

> Squeeze the buildings together again by adding two empty `div` elements within both the top and bottom of the `.foreground-buildings` element, and one more in between `.fb2` and `.fb3`.

Cambio en `index.html`:

```diff
@@ -25,15 +25,17 @@
     </div>
 
     <div class="foreground-buildings">
-
+      <div></div>
+      <div></div>
       <div class="fb1"></div>
       <div class="fb2"></div>
-
+      <div></div>
       <div class="fb3"></div>
       <div class="fb4"></div>
       <div class="fb5"></div>
       <div class="fb6"></div>
-
+      <div></div>
+      <div></div>
     </div>
   </body>
 </html>
```

Cambio en `styles.css`:

```diff
@@ -98,12 +98,14 @@
   width: 8%;
   height: 45%;
   background-color: var(--building-color1);
+
 }
 
 .fb5 {
   width: 10%;
   height: 33%;
   background-color: var(--building-color2);
+
 }
 
 .fb6 {
```

Código completo tras este paso: `pasos/paso-033/`

## Paso 34

> Move the position of `.fb4` relative to where it is now by adding a `position` of `relative` and `left` of `10%` to it. Do the same for `.fb5` but use `right` instead of `left`. This will cover up the remaining white space in between the buildings.

Cambio en `styles.css`:

```diff
@@ -25,6 +25,7 @@
   position: absolute;
   top: 0;
 }
+
 
 .bb1 {
   width: 10%;
@@ -76,6 +77,7 @@
   background-color: var(--building-color4);
 }
 
+
 .fb1 {
   width: 10%;
   height: 60%;
@@ -98,14 +100,16 @@
   width: 8%;
   height: 45%;
   background-color: var(--building-color1);
-
+  position: relative;
+  left: 10%;
 }
 
 .fb5 {
   width: 10%;
   height: 33%;
   background-color: var(--building-color2);
-
+  position: relative;
+  right: 10%;
 }
 
 .fb6 {
```

Código completo tras este paso: `pasos/paso-034/`

## Paso 35

> Your code is starting to get quite long. Add a comment above the `.fb1` class that says `FOREGROUND BUILDINGS - "fb" stands for "foreground building"` to help people understand your code. Above the `.bb1` class add another comment that says `BACKGROUND BUILDINGS - "bb" stands for "background building"`. If you don't remember, comments in CSS look like this: `/* Comment here */`.

Cambio en `styles.css`:

```diff
@@ -3,6 +3,7 @@
   --building-color2: #66cc99;
   --building-color3: #cc6699;
   --building-color4: #538cc6;
+
 }
 
 * {
@@ -26,7 +27,7 @@
   top: 0;
 }
 
-
+/* BACKGROUND BUILDINGS - "bb" stands for "background building" */
 .bb1 {
   width: 10%;
   height: 70%;
@@ -77,7 +78,7 @@
   background-color: var(--building-color4);
 }
 
-
+/* FOREGROUND BUILDINGS - "fb" stands for "foreground building" */
 .fb1 {
   width: 10%;
   height: 60%;
```

Código completo tras este paso: `pasos/paso-035/`

## Paso 36

> Create a new variable in `:root` called `--window-color1` and give it a value of `black`. This will be a secondary color for the purple buildings.

Cambio en `styles.css`:

```diff
@@ -3,7 +3,7 @@
   --building-color2: #66cc99;
   --building-color3: #cc6699;
   --building-color4: #538cc6;
-
+  --window-color1: black;
 }
 
 * {
@@ -40,6 +40,7 @@
   width: 70%;
   height: 10%;
   background-color: var(--building-color1);
+
 }
 
 .bb1b {
```

Código completo tras este paso: `pasos/paso-036/`

## Paso 37

> In a previous module you learned that gradients in CSS are a way to transition between colors across the distance of an element. They are applied to the `background` property and the syntax looks like this:
> 
> ```css
> gradient-type(
>   color1,
>   color2
> );
> ```
> 
> In the example, `color1` is solid at the top, `color2` is solid at the bottom, and in between it transitions evenly from one to the next. In `.bb1a`, add a `background` property below the `background-color` property. Set it as a gradient of type `linear-gradient` that uses `--building-color1` as the first color and `--window-color1` as the second.

Cambio en `styles.css`:

```diff
@@ -40,7 +40,10 @@
   width: 70%;
   height: 10%;
   background-color: var(--building-color1);
-
+  background: linear-gradient(
+      var(--building-color1),
+      var(--window-color1)
+    );
 }
 
 .bb1b {
@@ -60,6 +63,8 @@
   height: 70%;
   background-color: var(--building-color1);
 }
+
+
 
 .bb2 {
   width: 10%;
```

Código completo tras este paso: `pasos/paso-037/`

## Paso 38

> You want to add the same gradient to the next two sections. Instead of doing that, create a new class selector called `bb1-window`, and move the `height` and `background` properties and values from `.bb1a` to the new class selector.

Cambio en `styles.css`:

```diff
@@ -38,12 +38,7 @@
 
 .bb1a {
   width: 70%;
-  height: 10%;
   background-color: var(--building-color1);
-  background: linear-gradient(
-      var(--building-color1),
-      var(--window-color1)
-    );
 }
 
 .bb1b {
@@ -64,7 +59,13 @@
   background-color: var(--building-color1);
 }
 
-
+.bb1-window {
+  height: 10%;
+  background: linear-gradient(
+      var(--building-color1),
+      var(--window-color1)
+    );
+}
 
 .bb2 {
   width: 10%;
```

Código completo tras este paso: `pasos/paso-038/`

## Paso 39

> Add the new `bb1-window` class to the `.bb1a`, `.bb1b`, and `.bb1c` elements. This will apply the gradient to them.

Cambio en `index.html`:

```diff
@@ -11,9 +11,9 @@
       <div></div>
       <div></div>
       <div class="bb1">
-        <div class="bb1a"></div>
-        <div class="bb1b"></div>
-        <div class="bb1c"></div>
+        <div class="bb1a bb1-window"></div>
+        <div class="bb1b bb1-window"></div>
+        <div class="bb1c bb1-window"></div>
         <div class="bb1d"></div>
       </div>
       <div class="bb2"></div>
```

Código completo tras este paso: `pasos/paso-039/`

## Paso 40

> You don't need the `height` or `background-color` properties in `.bb1a`, `.bb1b` or `.bb1c` anymore, so go ahead and remove them.

Cambio en `styles.css`:

```diff
@@ -38,25 +38,21 @@
 
 .bb1a {
   width: 70%;
-  background-color: var(--building-color1);
 }
 
 .bb1b {
   width: 80%;
-  height: 10%;
-  background-color: var(--building-color1);
 }
 
 .bb1c {
   width: 90%;
-  height: 10%;
-  background-color: var(--building-color1);
 }
 
 .bb1d {
   width: 100%;
   height: 70%;
   background-color: var(--building-color1);
+
 }
 
 .bb1-window {
```

Código completo tras este paso: `pasos/paso-040/`

## Paso 41

> Gradients can use as many colors as you want like this:
> 
> ```css
> gradient-type(
>   color1,
>   color2,
>   color3
> );
> ```
> 
> Add a `linear-gradient` to `.bb1d` with `orange` as the first color, `--building-color1` as the second, and `--window-color1` as the third. Remember to use the gradient on the `background` property.

Cambio en `styles.css`:

```diff
@@ -52,7 +52,11 @@
   width: 100%;
   height: 70%;
   background-color: var(--building-color1);
-
+  background: linear-gradient(
+      orange,
+      var(--building-color1),
+      var(--window-color1)
+    );
 }
 
 .bb1-window {
```

Código completo tras este paso: `pasos/paso-041/`

## Paso 42

> It's a little hidden behind the foreground buildings, but you can see the three color gradient there. Since you are using that now, remove the `background-color` property from `.bb1d`.

Cambio en `styles.css`:

```diff
@@ -51,7 +51,6 @@
 .bb1d {
   width: 100%;
   height: 70%;
-  background-color: var(--building-color1);
   background: linear-gradient(
       orange,
       var(--building-color1),
```

Código completo tras este paso: `pasos/paso-042/`

## Paso 43

> You can specify where you want a gradient transition to complete by adding it to the color like this:
> 
> ```css
> gradient-type(
>   color1,
>   color2 20%,
>   color3
> );
> ```
> 
> Here, it will transition from `color1` to `color2` between `0%` and `20%` of the element and then transition to `color3` for the rest. Add `80%` to the `--building-color1` color of the `.bb1d` gradient so you can see it in action.

Cambio en `styles.css`:

```diff
@@ -53,7 +53,7 @@
   height: 70%;
   background: linear-gradient(
       orange,
-      var(--building-color1),
+      var(--building-color1) 80%,
       var(--window-color1)
     );
 }
```

Código completo tras este paso: `pasos/paso-043/`

## Paso 44

> Remove `orange` from the `.bb1d` gradient and change the `80%` to `50%`. This will make `--building-color1` solid for the top half, and then transition to `--window-color1` for the bottom half.

Cambio en `index.html`:

```diff
@@ -16,7 +16,9 @@
         <div class="bb1c bb1-window"></div>
         <div class="bb1d"></div>
       </div>
-      <div class="bb2"></div>
+      <div class="bb2">
+
+      </div>
       <div class="bb3"></div>
       <div></div>
       <div class="bb4"></div>
```

Cambio en `styles.css`:

```diff
@@ -52,8 +52,7 @@
   width: 100%;
   height: 70%;
   background: linear-gradient(
-      orange,
-      var(--building-color1) 80%,
+      var(--building-color1) 50%,
       var(--window-color1)
     );
 }
```

Código completo tras este paso: `pasos/paso-044/`

## Paso 45

> Nest two new `div` elements within `.bb2`, give them the classes of `bb2a` and `bb2b`, in that order. These will be two sections for this building.

Cambio en `index.html`:

```diff
@@ -17,7 +17,8 @@
         <div class="bb1d"></div>
       </div>
       <div class="bb2">
-
+        <div class="bb2a"></div>
+        <div class="bb2b"></div>
       </div>
       <div class="bb3"></div>
       <div></div>
```

Cambio en `styles.css`:

```diff
@@ -71,6 +71,8 @@
   background-color: var(--building-color2);
 }
 
+
+
 .bb3 {
   width: 10%;
   height: 55%;
```

Código completo tras este paso: `pasos/paso-045/`

## Paso 46

> Give `.bb2b` a `width` and `height` of `100%` to make it fill the building container. You will add something on the top a little later.

Cambio en `styles.css`:

```diff
@@ -4,6 +4,7 @@
   --building-color3: #cc6699;
   --building-color4: #538cc6;
   --window-color1: black;
+
 }
 
 * {
@@ -71,7 +72,10 @@
   background-color: var(--building-color2);
 }
 
-
+.bb2b {
+  width: 100%;
+  height: 100%;
+}
 
 .bb3 {
   width: 10%;
```

Código completo tras este paso: `pasos/paso-046/`

## Paso 47

> Create a new variable in `:root` named `window-color2` with a value of `#8cd9b3`. This will be used as the secondary color for this building.

Cambio en `styles.css`:

```diff
@@ -4,7 +4,7 @@
   --building-color3: #cc6699;
   --building-color4: #538cc6;
   --window-color1: black;
-
+  --window-color2: #8cd9b3;
 }
 
 * {
@@ -75,6 +75,7 @@
 .bb2b {
   width: 100%;
   height: 100%;
+
 }
 
 .bb3 {
```

Código completo tras este paso: `pasos/paso-047/`

## Paso 48

> Gradient transitions often gradually change from one color to another. When a more abrupt change is required, the transition can be made with a hard stop like this:
> 
> ```css
> linear-gradient(
>   var(--first-color) 0%,
>   var(--first-color) 40%,
>   var(--second-color) 40%,
>   var(--second-color) 80%
> );
> ```
> 
> Add a `linear-gradient` to `.bb2b` that uses `--building-color2` from `0%` to `6%` and `--window-color2` from `6%` to `9%`.

Cambio en `styles.css`:

```diff
@@ -75,7 +75,12 @@
 .bb2b {
   width: 100%;
   height: 100%;
-
+  background: linear-gradient(
+      var(--building-color2),
+      var(--building-color2) 6%,
+      var(--window-color2) 6%,
+      var(--window-color2) 9%
+    );
 }
 
 .bb3 {
```

Código completo tras este paso: `pasos/paso-048/`

## Paso 49

> You can see the hard color change at the top of the section. Change the gradient type from `linear-gradient` to `repeating-linear-gradient` for this section. This will make the four colors of your gradient repeat until it gets to the bottom of the element; giving you some stripes, and saving you from having to add a bunch of elements to create them.

Cambio en `styles.css`:

```diff
@@ -75,7 +75,7 @@
 .bb2b {
   width: 100%;
   height: 100%;
-  background: linear-gradient(
+  background: repeating-linear-gradient(
       var(--building-color2),
       var(--building-color2) 6%,
       var(--window-color2) 6%,
```

Código completo tras este paso: `pasos/paso-049/`

## Paso 50

> In the next few steps, you are going to use some tricks with CSS borders to turn the `.bb2a` section into a triangle at the top of the building. First, remove the `background-color` from `.bb2` since you don't need it anymore.

Cambio en `styles.css`:

```diff
@@ -69,8 +69,9 @@
 .bb2 {
   width: 10%;
   height: 50%;
-  background-color: var(--building-color2);
 }
+
+
 
 .bb2b {
   width: 100%;
```

Código completo tras este paso: `pasos/paso-050/`

## Paso 51

> Create and add the following properties to `.bb2a`:
> 
> ```css
> margin: auto;
> width: 5vw;
> height: 5vw;
> border-top: 1vw solid #000;
> border-bottom: 1vw solid #000;
> border-left: 1vw solid #999;
> border-right: 1vw solid #999;
> ```
> 
> After you add these, you can see how a thick border on an element gives you some angles where two sides meet. You are going to use that bottom border as the top of the building.

Cambio en `styles.css`:

```diff
@@ -71,7 +71,15 @@
   height: 50%;
 }
 
-
+.bb2a {
+  margin: auto;
+  width: 5vw;
+  height: 5vw;
+  border-top: 1vw solid #000;
+  border-bottom: 1vw solid #000;
+  border-left: 1vw solid #999;
+  border-right: 1vw solid #999;
+}
 
 .bb2b {
   width: 100%;
```

Código completo tras este paso: `pasos/paso-051/`

## Paso 52

> Next, remove the `width` and `height` from `.bb2a`, and change the `border-left` and `border-right` to use `5vw` instead of `1vw`. The element will now have zero size and the borders will come together in the middle.

Cambio en `styles.css`:

```diff
@@ -73,12 +73,10 @@
 
 .bb2a {
   margin: auto;
-  width: 5vw;
-  height: 5vw;
   border-top: 1vw solid #000;
   border-bottom: 1vw solid #000;
-  border-left: 1vw solid #999;
-  border-right: 1vw solid #999;
+  border-left: 5vw solid #999;
+  border-right: 5vw solid #999;
 }
 
 .bb2b {
```

Código completo tras este paso: `pasos/paso-052/`

## Paso 53

> Next, change the two `#999` of `.bb2a` to `transparent`. This will make the left and right borders invisible.

Cambio en `styles.css`:

```diff
@@ -75,8 +75,8 @@
   margin: auto;
   border-top: 1vw solid #000;
   border-bottom: 1vw solid #000;
-  border-left: 5vw solid #999;
-  border-right: 5vw solid #999;
+  border-left: 5vw solid transparent;
+  border-right: 5vw solid transparent;
 }
 
 .bb2b {
```

Código completo tras este paso: `pasos/paso-053/`

## Paso 54

> Remove the `margin` and `border-top` properties and values from `.bb2a` to turn it into a triangle for the top of the building.

Cambio en `styles.css`:

```diff
@@ -72,8 +72,6 @@
 }
 
 .bb2a {
-  margin: auto;
-  border-top: 1vw solid #000;
   border-bottom: 1vw solid #000;
   border-left: 5vw solid transparent;
   border-right: 5vw solid transparent;
```

Código completo tras este paso: `pasos/paso-054/`

## Paso 55

> Finally, on the `border-bottom` property of `.bb2a`, change the `1vw` to `5vh` and change the `#000` color to your `--building-color2` variable. There you go, now it looks good! At any time throughout this project, you can comment out or remove the `border` property you added to everything at the beginning to see what the buildings will look like when that gets removed at the end.

Cambio en `styles.css`:

```diff
@@ -5,6 +5,7 @@
   --building-color4: #538cc6;
   --window-color1: black;
   --window-color2: #8cd9b3;
+
 }
 
 * {
@@ -72,7 +73,7 @@
 }
 
 .bb2a {
-  border-bottom: 1vw solid #000;
+  border-bottom: 5vh solid var(--building-color2);
   border-left: 5vw solid transparent;
   border-right: 5vw solid transparent;
 }
```

Código completo tras este paso: `pasos/paso-055/`

## Paso 56

> On to the next building! Create a new variable called `--window-color3` in `:root` and give it a value of `#d98cb3`. This will be the secondary color for the pink buildings.

Cambio en `styles.css`:

```diff
@@ -5,7 +5,7 @@
   --building-color4: #538cc6;
   --window-color1: black;
   --window-color2: #8cd9b3;
-
+  --window-color3: #d98cb3;
 }
 
 * {
@@ -93,6 +93,7 @@
   width: 10%;
   height: 55%;
   background-color: var(--building-color3);
+
 }
 
 .bb4 {
```

Código completo tras este paso: `pasos/paso-056/`

## Paso 57

> So far, all the gradients you created have gone from top to bottom, that's the default direction. You can specify another direction by adding it before your colors like this:
> 
> ```css
> gradient-type(
>   direction,
>   color1,
>   color2
> );
> ```
> 
> Fill in `.bb3` with a `repeating-linear-gradient`. Use `90deg` for the direction, your `building-color3` for the first two colors, and `window-color3` at `15%` for the third. When you don't specify a distance for a color, it will use the values that make sense. In this case, the first two colors will default to `0%` and `7.5%` because it starts at `0%`, and `7.5%` is half of the `15%`.

Cambio en `styles.css`:

```diff
@@ -93,7 +93,12 @@
   width: 10%;
   height: 55%;
   background-color: var(--building-color3);
-
+  background: repeating-linear-gradient(
+      90deg,
+      var(--building-color3),
+      var(--building-color3),
+      var(--window-color3) 15%
+    );
 }
 
 .bb4 {
```

Código completo tras este paso: `pasos/paso-057/`

## Paso 58

> Remove the `background-color` property and value from `.bb3` since you are using the gradient as the background now.

Cambio en `index.html`:

```diff
@@ -22,7 +22,9 @@
       </div>
       <div class="bb3"></div>
       <div></div>
-      <div class="bb4"></div>
+      <div class="bb4">
+
+      </div>
       <div></div>
       <div></div>
     </div>
```

Cambio en `styles.css`:

```diff
@@ -92,7 +92,6 @@
 .bb3 {
   width: 10%;
   height: 55%;
-  background-color: var(--building-color3);
   background: repeating-linear-gradient(
       90deg,
       var(--building-color3),
```

Código completo tras este paso: `pasos/paso-058/`

## Paso 59

> The next building will have three sections. Nest three `div` elements within `.bb4`. Give them the classes of `bb4a`, `bb4b` and `bb4c` in that order.

Cambio en `index.html`:

```diff
@@ -23,7 +23,9 @@
       <div class="bb3"></div>
       <div></div>
       <div class="bb4">
-
+        <div class="bb4a"></div>
+        <div class="bb4b"></div>
+        <div class="bb4c"></div>
       </div>
       <div></div>
       <div></div>
```

Cambio en `styles.css`:

```diff
@@ -106,6 +106,8 @@
   background-color: var(--building-color4);
 }
 
+
+
 /* FOREGROUND BUILDINGS - "fb" stands for "foreground building" */
 .fb1 {
   width: 10%;
```

Código completo tras este paso: `pasos/paso-059/`

## Paso 60

> Give the new `div` elements these `width` and `height` values: `3%` and `10%` to `.bb4a`, `80%` and `5%` to `.bb4b`, and `100%` and `85%` to `.bb4c`.

Cambio en `styles.css`:

```diff
@@ -106,7 +106,23 @@
   background-color: var(--building-color4);
 }
 
+.bb4a {
+  width: 3%;
+  height: 10%;
 
+}
+
+.bb4b {
+  width: 80%;
+  height: 5%;
+
+}
+
+.bb4c {
+  width: 100%;
+  height: 85%;
+
+}
 
 /* FOREGROUND BUILDINGS - "fb" stands for "foreground building" */
 .fb1 {
```

Código completo tras este paso: `pasos/paso-060/`

## Paso 61

> Remove the `background-color` property and value from `.bb4`, and add it to the three new sections `.bb4a`, `.bb4b`, and `.bb4c`, so only the sections are filled.

Cambio en `styles.css`:

```diff
@@ -28,6 +28,8 @@
   position: absolute;
   top: 0;
 }
+
+
 
 /* BACKGROUND BUILDINGS - "bb" stands for "background building" */
 .bb1 {
@@ -103,25 +105,24 @@
 .bb4 {
   width: 11%;
   height: 58%;
-  background-color: var(--building-color4);
 }
 
 .bb4a {
   width: 3%;
   height: 10%;
-
+  background-color: var(--building-color4);
 }
 
 .bb4b {
   width: 80%;
   height: 5%;
-
+  background-color: var(--building-color4);
 }
 
 .bb4c {
   width: 100%;
   height: 85%;
-
+  background-color: var(--building-color4);
 }
 
 /* FOREGROUND BUILDINGS - "fb" stands for "foreground building" */
```

Código completo tras este paso: `pasos/paso-061/`

## Paso 62

> You want `.bb4` to share the properties of `.bb1` that center the sections. Instead of duplicating that code, create a new class above the background building comment called `building-wrap`. Leave it empty for now; this class will be used in a few places to save you some coding.

Cambio en `styles.css`:

```diff
@@ -29,7 +29,9 @@
   top: 0;
 }
 
+.building-wrap {
 
+}
 
 /* BACKGROUND BUILDINGS - "bb" stands for "background building" */
 .bb1 {
```

Código completo tras este paso: `pasos/paso-062/`

## Paso 63

> Move the `display`, `flex-direction`, and `align-items` properties and values from `.bb1` to the new `building-wrap` class.

Cambio en `styles.css`:

```diff
@@ -30,16 +30,15 @@
 }
 
 .building-wrap {
-
+  display: flex;
+  flex-direction: column;
+  align-items: center;
 }
 
 /* BACKGROUND BUILDINGS - "bb" stands for "background building" */
 .bb1 {
   width: 10%;
   height: 70%;
-  display: flex;
-  flex-direction: column;
-  align-items: center;
 }
 
 .bb1a {
```

Código completo tras este paso: `pasos/paso-063/`

## Paso 64

> Add the new `building-wrap` class to the `.bb1` and `.bb4` elements. This will apply the centering properties to the buildings that need it.

Cambio en `index.html`:

```diff
@@ -10,7 +10,7 @@
     <div class="background-buildings">
       <div></div>
       <div></div>
-      <div class="bb1">
+      <div class="bb1 building-wrap">
         <div class="bb1a bb1-window"></div>
         <div class="bb1b bb1-window"></div>
         <div class="bb1c bb1-window"></div>
@@ -22,7 +22,7 @@
       </div>
       <div class="bb3"></div>
       <div></div>
-      <div class="bb4">
+      <div class="bb4 building-wrap">
         <div class="bb4a"></div>
         <div class="bb4b"></div>
         <div class="bb4c"></div>
```

Cambio en `styles.css`:

```diff
@@ -6,6 +6,7 @@
   --window-color1: black;
   --window-color2: #8cd9b3;
   --window-color3: #d98cb3;
+
 }
 
 * {
```

Código completo tras este paso: `pasos/paso-064/`

## Paso 65

> Create a new variable called `--window-color4` in `:root` and give it a value of `#8cb3d9`. This will be the secondary color for the last background building.

Cambio en `index.html`:

```diff
@@ -25,7 +25,9 @@
       <div class="bb4 building-wrap">
         <div class="bb4a"></div>
         <div class="bb4b"></div>
-        <div class="bb4c"></div>
+        <div class="bb4c">
+
+        </div>
       </div>
       <div></div>
       <div></div>
```

Cambio en `styles.css`:

```diff
@@ -6,7 +6,7 @@
   --window-color1: black;
   --window-color2: #8cd9b3;
   --window-color3: #d98cb3;
-
+  --window-color4: #8cb3d9;
 }
 
 * {
```

Código completo tras este paso: `pasos/paso-065/`

## Paso 66

> Nest four new `div` elements within `.bb4c`, give them all the class of `bb4-window`. These will be windows for this building.

Cambio en `index.html`:

```diff
@@ -26,7 +26,10 @@
         <div class="bb4a"></div>
         <div class="bb4b"></div>
         <div class="bb4c">
-
+          <div class="bb4-window"></div>
+          <div class="bb4-window"></div>
+          <div class="bb4-window"></div>
+          <div class="bb4-window"></div>
         </div>
       </div>
       <div></div>
```

Cambio en `styles.css`:

```diff
@@ -127,6 +127,8 @@
   background-color: var(--building-color4);
 }
 
+
+
 /* FOREGROUND BUILDINGS - "fb" stands for "foreground building" */
 .fb1 {
   width: 10%;
```

Código completo tras este paso: `pasos/paso-066/`

## Paso 67

> Give the `bb4-window` class a `width` of `18%`, a `height` of `90%`, and add your `--window-color4` variable as the `background-color`.

Cambio en `styles.css`:

```diff
@@ -35,6 +35,8 @@
   flex-direction: column;
   align-items: center;
 }
+
+
 
 /* BACKGROUND BUILDINGS - "bb" stands for "background building" */
 .bb1 {
@@ -127,7 +129,11 @@
   background-color: var(--building-color4);
 }
 
-
+.bb4-window {
+  width: 18%;
+  height: 90%;
+  background-color: var(--window-color4);
+}
 
 /* FOREGROUND BUILDINGS - "fb" stands for "foreground building" */
 .fb1 {
```

Código completo tras este paso: `pasos/paso-067/`

## Paso 68

> The windows are stacked on top of each other at the left of the section, behind the purple building. Add a new class below `.building-wrap` called `window-wrap`. Make `.window-wrap` a flexbox container, and use the `align-items` and `justify-content` properties to center its child elements vertically and evenly space them in their parent, respectively.

Cambio en `styles.css`:

```diff
@@ -36,7 +36,11 @@
   align-items: center;
 }
 
-
+.window-wrap {
+  display: flex;
+  align-items: center;
+  justify-content: space-evenly;
+}
 
 /* BACKGROUND BUILDINGS - "bb" stands for "background building" */
 .bb1 {
```

Código completo tras este paso: `pasos/paso-068/`

## Paso 69

> Add the new `window-wrap` class to the `.bb4c` element.

Cambio en `index.html`:

```diff
@@ -25,7 +25,7 @@
       <div class="bb4 building-wrap">
         <div class="bb4a"></div>
         <div class="bb4b"></div>
-        <div class="bb4c">
+        <div class="bb4c window-wrap">
           <div class="bb4-window"></div>
           <div class="bb4-window"></div>
           <div class="bb4-window"></div>
@@ -39,7 +39,9 @@
     <div class="foreground-buildings">
       <div></div>
       <div></div>
-      <div class="fb1"></div>
+      <div class="fb1">
+
+      </div>
       <div class="fb2"></div>
       <div></div>
       <div class="fb3"></div>
```

Código completo tras este paso: `pasos/paso-069/`

## Paso 70

> Looks good! On to the foreground buildings! Turn the `.fb1` building into three sections by nesting three new `div` elements within it. Give them the classes of `fb1a`, `fb1b` and `fb1c`, in that order.

Cambio en `index.html`:

```diff
@@ -40,7 +40,9 @@
       <div></div>
       <div></div>
       <div class="fb1">
-
+        <div class="fb1a"></div>
+        <div class="fb1b"></div>
+        <div class="fb1c"></div>
       </div>
       <div class="fb2"></div>
       <div></div>
```

Cambio en `styles.css`:

```diff
@@ -146,6 +146,8 @@
   background-color: var(--building-color4);
 }
 
+
+
 .fb2 {
   width: 10%;
   height: 40%;
```

Código completo tras este paso: `pasos/paso-070/`

## Paso 71

> Give `.fb1b` a `width` of `60%` and `height` of `10%`, and `.fb1c` a `width` of `100%` and `height` of `80%`.

Cambio en `styles.css`:

```diff
@@ -146,7 +146,15 @@
   background-color: var(--building-color4);
 }
 
+.fb1b {
+  width: 60%;
+  height: 10%;
+}
 
+.fb1c {
+  width: 100%;
+  height: 80%;
+}
 
 .fb2 {
   width: 10%;
```

Código completo tras este paso: `pasos/paso-071/`

## Paso 72

> Add the `building-wrap` class to the `.fb1` element to center the sections.

Cambio en `index.html`:

```diff
@@ -39,7 +39,7 @@
     <div class="foreground-buildings">
       <div></div>
       <div></div>
-      <div class="fb1">
+      <div class="fb1 building-wrap">
         <div class="fb1a"></div>
         <div class="fb1b"></div>
         <div class="fb1c"></div>
```

Cambio en `styles.css`:

```diff
@@ -149,6 +149,7 @@
 .fb1b {
   width: 60%;
   height: 10%;
+
 }
 
 .fb1c {
```

Código completo tras este paso: `pasos/paso-072/`

## Paso 73

> Move the `background-color` property and value from `.fb1` to `.fb1b`.

Cambio en `styles.css`:

```diff
@@ -143,18 +143,18 @@
 .fb1 {
   width: 10%;
   height: 60%;
-  background-color: var(--building-color4);
 }
 
 .fb1b {
   width: 60%;
   height: 10%;
-
+  background-color: var(--building-color4);
 }
 
 .fb1c {
   width: 100%;
   height: 80%;
+
 }
 
 .fb2 {
```

Código completo tras este paso: `pasos/paso-073/`

## Paso 74

> Don't worry about the space at the bottom, everything will get moved down later when you add some height to the element at the top of the building.
> 
> Add a `repeating-linear-gradient` to `.fb1c` with a `90deg` angle, your `--building-color4` from `0%` to `10%` and `transparent` from `10%` to `15%`.

Cambio en `styles.css`:

```diff
@@ -154,7 +154,13 @@
 .fb1c {
   width: 100%;
   height: 80%;
-
+  background: repeating-linear-gradient(
+      90deg,
+      var(--building-color4),
+      var(--building-color4) 10%,
+      transparent 10%,
+      transparent 15%
+    )
 }
 
 .fb2 {
```

Código completo tras este paso: `pasos/paso-074/`

## Paso 75

> You can add multiple gradients to an element by separating them with a comma (`,`) like this:
> 
> ```css
> gradient1(
>   colors
> ),
> gradient2(
>   colors
> );
> ```
> 
> Add a `repeating-linear-gradient` to `.fb1c` below the one that's there; use your `--building-color4` from `0%` to `10%` and `--window-color4` from `10%` and `90%`. This will fill in behind the gradient you added last.

Cambio en `styles.css`:

```diff
@@ -145,6 +145,8 @@
   height: 60%;
 }
 
+
+
 .fb1b {
   width: 60%;
   height: 10%;
@@ -160,7 +162,13 @@
       var(--building-color4) 10%,
       transparent 10%,
       transparent 15%
-    )
+    ),
+    repeating-linear-gradient(
+      var(--building-color4),
+      var(--building-color4) 10%,
+      var(--window-color4) 10%,
+      var(--window-color4) 90%
+    );
 }
 
 .fb2 {
```

Código completo tras este paso: `pasos/paso-075/`

## Paso 76

> You're going to use some more border tricks for the top section. Add a `border-bottom` with a value of `7vh solid var(--building-color4)` to `.fb1a`. This will put a `7vh` height border on the bottom. But since the element has zero size, it only shows up as a 2px wide line from the 1px border that is on all the elements.

Cambio en `styles.css`:

```diff
@@ -145,7 +145,10 @@
   height: 60%;
 }
 
-
+.fb1a {
+  border-bottom: 7vh solid var(--building-color4);
+
+}
 
 .fb1b {
   width: 60%;
```

Código completo tras este paso: `pasos/paso-076/`

## Paso 77

> When you increase the size of the left and right borders, the border on the bottom will expand to be the width of the combined left and right border widths. Add `2vw solid transparent` as the value of the `border-left` and `border-right` properties of `.fb1a`. They will be invisible, but it will make the border on the bottom `4vw` wide.

Cambio en `index.html`:

```diff
@@ -44,7 +44,9 @@
         <div class="fb1b"></div>
         <div class="fb1c"></div>
       </div>
-      <div class="fb2"></div>
+      <div class="fb2">
+
+      </div>
       <div></div>
       <div class="fb3"></div>
       <div class="fb4"></div>
```

Cambio en `styles.css`:

```diff
@@ -147,7 +147,8 @@
 
 .fb1a {
   border-bottom: 7vh solid var(--building-color4);
-
+  border-left: 2vw solid transparent;
+  border-right: 2vw solid transparent;
 }
 
 .fb1b {
```

Código completo tras este paso: `pasos/paso-077/`

## Paso 78

> On to the next building! Nest two `div` elements within `.fb2` and give them classes of `fb2a` and `fb2b`, in that order.

Cambio en `index.html`:

```diff
@@ -45,7 +45,8 @@
         <div class="fb1c"></div>
       </div>
       <div class="fb2">
-
+        <div class="fb2a"></div>
+        <div class="fb2b"></div>
       </div>
       <div></div>
       <div class="fb3"></div>
```

Cambio en `styles.css`:

```diff
@@ -181,6 +181,8 @@
   background-color: var(--building-color3);
 }
 
+
+
 .fb3 {
   width: 10%;
   height: 35%;
```

Código completo tras este paso: `pasos/paso-078/`

## Paso 79

> Give `.fb2a` a `width` of `100%` and `.fb2b` a `width` of `100%` and `height` of `75%`.

Cambio en `index.html`:

```diff
@@ -46,7 +46,9 @@
       </div>
       <div class="fb2">
         <div class="fb2a"></div>
-        <div class="fb2b"></div>
+        <div class="fb2b">
+
+        </div>
       </div>
       <div></div>
       <div class="fb3"></div>
```

Cambio en `styles.css`:

```diff
@@ -181,7 +181,14 @@
   background-color: var(--building-color3);
 }
 
-
+.fb2a {
+  width: 100%;
+}
+
+.fb2b {
+  width: 100%;
+  height: 75%;
+}
 
 .fb3 {
   width: 10%;
```

Código completo tras este paso: `pasos/paso-079/`

## Paso 80

> Nest three `div` elements within `.fb2b` and give them a class of `fb2-window`. These will be windows for this section of the building.

Cambio en `index.html`:

```diff
@@ -47,7 +47,9 @@
       <div class="fb2">
         <div class="fb2a"></div>
         <div class="fb2b">
-
+          <div class="fb2-window"></div>
+          <div class="fb2-window"></div>
+          <div class="fb2-window"></div>
         </div>
       </div>
       <div></div>
```

Código completo tras este paso: `pasos/paso-080/`

## Paso 81

> Add your `window-wrap` class to `.fb2b` to position the new window elements.

Cambio en `index.html`:

```diff
@@ -46,7 +46,7 @@
       </div>
       <div class="fb2">
         <div class="fb2a"></div>
-        <div class="fb2b">
+        <div class="fb2b window-wrap">
           <div class="fb2-window"></div>
           <div class="fb2-window"></div>
           <div class="fb2-window"></div>
```

Cambio en `styles.css`:

```diff
@@ -190,6 +190,8 @@
   height: 75%;
 }
 
+
+
 .fb3 {
   width: 10%;
   height: 35%;
```

Código completo tras este paso: `pasos/paso-081/`

## Paso 82

> Give the `.fb2-window` elements a `width` of `22%`, `height` of `100%`, and a `background-color` of your `--window-color3` variable.

Cambio en `styles.css`:

```diff
@@ -188,9 +188,14 @@
 .fb2b {
   width: 100%;
   height: 75%;
-}
-
-
+
+}
+
+.fb2-window {
+  width: 22%;
+  height: 100%;
+  background-color: var(--window-color3);
+}
 
 .fb3 {
   width: 10%;
```

Código completo tras este paso: `pasos/paso-082/`

## Paso 83

> Move the `background-color` property and value from `.fb2` to `.fb2b` to just color the section and not the container.

Cambio en `styles.css`:

```diff
@@ -178,17 +178,17 @@
 .fb2 {
   width: 10%;
   height: 40%;
+}
+
+.fb2a {
+  width: 100%;
+
+}
+
+.fb2b {
+  width: 100%;
+  height: 75%;
   background-color: var(--building-color3);
-}
-
-.fb2a {
-  width: 100%;
-}
-
-.fb2b {
-  width: 100%;
-  height: 75%;
-
 }
 
 .fb2-window {
```

Código completo tras este paso: `pasos/paso-083/`

## Paso 84

> For `.fb2a`, add a `border-bottom` of `10vh solid var(--building-color3)`, and a `border-left` and `border-right` of `1vw solid transparent`. This time the border trick will create a trapezoid shape.

Cambio en `index.html`:

```diff
@@ -53,7 +53,9 @@
         </div>
       </div>
       <div></div>
-      <div class="fb3"></div>
+      <div class="fb3">
+
+      </div>
       <div class="fb4"></div>
       <div class="fb5"></div>
       <div class="fb6"></div>
```

Cambio en `styles.css`:

```diff
@@ -182,7 +182,9 @@
 
 .fb2a {
   width: 100%;
-
+  border-bottom: 10vh solid var(--building-color3);
+  border-left: 1vw solid transparent;
+  border-right: 1vw solid transparent;
 }
 
 .fb2b {
```

Código completo tras este paso: `pasos/paso-084/`

## Paso 85

> For the next building, nest four `div` elements within `.fb3` with classes of `fb3a`, `fb3b`, `fb3a` again, and `fb3b` again, in that order. This building will have four sections, and the top two will be almost the same as the bottom two.

Cambio en `index.html`:

```diff
@@ -54,7 +54,10 @@
       </div>
       <div></div>
       <div class="fb3">
-
+        <div class="fb3a"></div>
+        <div class="fb3b"></div>
+        <div class="fb3a"></div>
+        <div class="fb3b"></div>
       </div>
       <div class="fb4"></div>
       <div class="fb5"></div>
```

Cambio en `styles.css`:

```diff
@@ -205,6 +205,8 @@
   background-color: var(--building-color1);
 }
 
+
+
 .fb4 {
   width: 8%;
   height: 45%;
```

Código completo tras este paso: `pasos/paso-085/`

## Paso 86

> Give the `.fb3a` element a `width` of `80%` and `height` of `15%`. Then give the `.fb3b` element a `width` of `100%` and `height` of `35%`.

Cambio en `styles.css`:

```diff
@@ -205,7 +205,17 @@
   background-color: var(--building-color1);
 }
 
-
+.fb3a {
+  width: 80%;
+  height: 15%;
+
+}
+
+.fb3b {
+  width: 100%;
+  height: 35%;
+
+}
 
 .fb4 {
   width: 8%;
```

Código completo tras este paso: `pasos/paso-086/`

## Paso 87

> Remove the `background-color` property and value from `.fb3`, and add them to `.fb3a` and `.fb3b`.

Cambio en `styles.css`:

```diff
@@ -202,19 +202,18 @@
 .fb3 {
   width: 10%;
   height: 35%;
-  background-color: var(--building-color1);
 }
 
 .fb3a {
   width: 80%;
   height: 15%;
-
+  background-color: var(--building-color1);
 }
 
 .fb3b {
   width: 100%;
   height: 35%;
-
+  background-color: var(--building-color1);
 }
 
 .fb4 {
```

Código completo tras este paso: `pasos/paso-087/`

## Paso 88

> Add your `building-wrap` class to the `.fb3` element to center the sections.

Cambio en `index.html`:

```diff
@@ -53,8 +53,10 @@
         </div>
       </div>
       <div></div>
-      <div class="fb3">
-        <div class="fb3a"></div>
+      <div class="fb3 building-wrap">
+        <div class="fb3a">
+
+        </div>
         <div class="fb3b"></div>
         <div class="fb3a"></div>
         <div class="fb3b"></div>
```

Código completo tras este paso: `pasos/paso-088/`

## Paso 89

> Nest three new `div` elements in the first `.fb3a` element. Give them each a class of `fb3-window`. These will be windows for this section.

Cambio en `index.html`:

```diff
@@ -55,7 +55,9 @@
       <div></div>
       <div class="fb3 building-wrap">
         <div class="fb3a">
-
+          <div class="fb3-window"></div>
+          <div class="fb3-window"></div>
+          <div class="fb3-window"></div>
         </div>
         <div class="fb3b"></div>
         <div class="fb3a"></div>
```

Cambio en `styles.css`:

```diff
@@ -216,6 +216,8 @@
   background-color: var(--building-color1);
 }
 
+
+
 .fb4 {
   width: 8%;
   height: 45%;
```

Código completo tras este paso: `pasos/paso-089/`

## Paso 90

> Give the `.fb3-window` elements a `width` of `25%`, a `height` of `80%`, and use your `--window-color1` variable as the `background-color` value.

Cambio en `styles.css`:

```diff
@@ -216,7 +216,11 @@
   background-color: var(--building-color1);
 }
 
-
+.fb3-window {
+  width: 25%;
+  height: 80%;
+  background-color: var(--window-color1);
+}
 
 .fb4 {
   width: 8%;
```

Código completo tras este paso: `pasos/paso-090/`

## Paso 91

> Add your `window-wrap` class to the `.fb3a` element to center and space the windows.

Cambio en `index.html`:

```diff
@@ -54,7 +54,7 @@
       </div>
       <div></div>
       <div class="fb3 building-wrap">
-        <div class="fb3a">
+        <div class="fb3a window-wrap">
           <div class="fb3-window"></div>
           <div class="fb3-window"></div>
           <div class="fb3-window"></div>
```

Código completo tras este paso: `pasos/paso-091/`

## Paso 92

> With CSS variables you can change values without searching everywhere in the stylesheet. Change the `--window-color1` value to `#bb99ff`.

Cambio en `index.html`:

```diff
@@ -63,7 +63,9 @@
         <div class="fb3a"></div>
         <div class="fb3b"></div>
       </div>
-      <div class="fb4"></div>
+      <div class="fb4">
+
+      </div>
       <div class="fb5"></div>
       <div class="fb6"></div>
       <div></div>
```

Cambio en `styles.css`:

```diff
@@ -3,7 +3,7 @@
   --building-color2: #66cc99;
   --building-color3: #cc6699;
   --building-color4: #538cc6;
-  --window-color1: black;
+  --window-color1: #bb99ff;
   --window-color2: #8cd9b3;
   --window-color3: #d98cb3;
   --window-color4: #8cb3d9;
```

Código completo tras este paso: `pasos/paso-092/`

## Paso 93

> Only three more buildings to go. Nest two new `div` elements within the `.fb4` element and give them the classes of `fb4a` and `fb4b`, in that order. Remember that you sort of flipped the location of `.fb4` and `.fb5`, so it's the rightmost purple building you are working on now.

Cambio en `index.html`:

```diff
@@ -64,7 +64,8 @@
         <div class="fb3b"></div>
       </div>
       <div class="fb4">
-
+        <div class="fb4a"></div>
+        <div class="fb4b"></div>
       </div>
       <div class="fb5"></div>
       <div class="fb6"></div>
```

Cambio en `styles.css`:

```diff
@@ -230,6 +230,8 @@
   left: 10%;
 }
 
+
+
 .fb5 {
   width: 10%;
   height: 33%;
```

Código completo tras este paso: `pasos/paso-093/`

## Paso 94

> Give `.fb4b` a `width` of `100%` and `height` of `89%`.

Cambio en `styles.css`:

```diff
@@ -230,7 +230,11 @@
   left: 10%;
 }
 
-
+.fb4b {
+  width: 100%;
+  height: 89%;
+
+}
 
 .fb5 {
   width: 10%;
```

Código completo tras este paso: `pasos/paso-094/`

## Paso 95

> Add your `--building-color1` variable as value of the `background-color` property of `.fb4b`. Then, remove the `background-color` from `.fb4`.

Cambio en `index.html`:

```diff
@@ -65,7 +65,9 @@
       </div>
       <div class="fb4">
         <div class="fb4a"></div>
-        <div class="fb4b"></div>
+        <div class="fb4b">
+
+        </div>
       </div>
       <div class="fb5"></div>
       <div class="fb6"></div>
```

Cambio en `styles.css`:

```diff
@@ -225,7 +225,6 @@
 .fb4 {
   width: 8%;
   height: 45%;
-  background-color: var(--building-color1);
   position: relative;
   left: 10%;
 }
@@ -233,7 +232,7 @@
 .fb4b {
   width: 100%;
   height: 89%;
-
+  background-color: var(--building-color1);
 }
 
 .fb5 {
```

Código completo tras este paso: `pasos/paso-095/`

## Paso 96

> Nest six `div` elements within `.fb4b` and give them all a class of `fb4-window`.

Cambio en `index.html`:

```diff
@@ -66,7 +66,12 @@
       <div class="fb4">
         <div class="fb4a"></div>
         <div class="fb4b">
-
+          <div class="fb4-window"></div>
+          <div class="fb4-window"></div>
+          <div class="fb4-window"></div>
+          <div class="fb4-window"></div>
+          <div class="fb4-window"></div>
+          <div class="fb4-window"></div>
         </div>
       </div>
       <div class="fb5"></div>
```

Cambio en `styles.css`:

```diff
@@ -235,6 +235,8 @@
   background-color: var(--building-color1);
 }
 
+
+
 .fb5 {
   width: 10%;
   height: 33%;
```

Código completo tras este paso: `pasos/paso-096/`

## Paso 97

> Give the `.fb4-window` elements a `width` of `30%`, `height` of `10%`, and `border-radius` of `50%`. These will make some circular windows for this building.

Cambio en `styles.css`:

```diff
@@ -235,7 +235,12 @@
   background-color: var(--building-color1);
 }
 
-
+.fb4-window {
+  width: 30%;
+  height: 10%;
+  border-radius: 50%;
+
+}
 
 .fb5 {
   width: 10%;
```

Código completo tras este paso: `pasos/paso-097/`

## Paso 98

> Fill in the windows with your secondary color for this building. Also add a `margin` of `10%` to give the windows some space.

Cambio en `styles.css`:

```diff
@@ -233,13 +233,15 @@
   width: 100%;
   height: 89%;
   background-color: var(--building-color1);
+
 }
 
 .fb4-window {
   width: 30%;
   height: 10%;
   border-radius: 50%;
-
+  background-color: var(--window-color1);
+  margin: 10%;
 }
 
 .fb5 {
```

Código completo tras este paso: `pasos/paso-098/`

## Paso 99

> The windows are stacked on top of each other on the rightmost purple building. Turn the building into a flexbox parent, and use the `flex-wrap` property to put the windows side by side, and push them down to a new row when they don't fit.

Cambio en `styles.css`:

```diff
@@ -229,11 +229,14 @@
   left: 10%;
 }
 
+
+
 .fb4b {
   width: 100%;
   height: 89%;
   background-color: var(--building-color1);
-
+  display: flex;
+  flex-wrap: wrap;
 }
 
 .fb4-window {
```

Código completo tras este paso: `pasos/paso-099/`

## Paso 100

> This building is going to have another triangle on top. Give the top section a `border-top` of `5vh solid transparent`, and a `border-left` that is `8vw`, `solid`, and uses your building color variable as the color.

Cambio en `styles.css`:

```diff
@@ -229,7 +229,10 @@
   left: 10%;
 }
 
-
+.fb4a {
+  border-top: 5vh solid transparent;
+  border-left: 8vw solid var(--building-color1);
+}
 
 .fb4b {
   width: 100%;
@@ -253,6 +256,7 @@
   background-color: var(--building-color2);
   position: relative;
   right: 10%;
+
 }
 
 .fb6 {
```

Código completo tras este paso: `pasos/paso-100/`

## Paso 101

> On to the next building! It's the green one in the foreground. Give it a `repeating-linear-gradient` with your building color from `0%` to `5%`, and `transparent` from `5%` to `10%`.

Cambio en `styles.css`:

```diff
@@ -256,7 +256,12 @@
   background-color: var(--building-color2);
   position: relative;
   right: 10%;
-
+  background: repeating-linear-gradient(
+      var(--building-color2),
+      var(--building-color2) 5%,
+      transparent 5%,
+      transparent 10%
+    )
 }
 
 .fb6 {
```

Código completo tras este paso: `pasos/paso-101/`

## Paso 102

> Add another `repeating-linear-gradient` below the one you just added. Give it a `90deg` direction, use your building color from `0%` to `12%` and window color `12%` to `44%`. This will make a bunch of rectangle windows.

Cambio en `styles.css`:

```diff
@@ -261,7 +261,14 @@
       var(--building-color2) 5%,
       transparent 5%,
       transparent 10%
-    )
+    ),
+    repeating-linear-gradient(
+      90deg,
+      var(--building-color2),
+      var(--building-color2) 12%,
+      var(--window-color2) 12%,
+      var(--window-color2) 44%
+    );
 }
 
 .fb6 {
```

Código completo tras este paso: `pasos/paso-102/`

## Paso 103

> You don't need the `background-color` for this building anymore so you can remove that property.

Cambio en `styles.css`:

```diff
@@ -253,7 +253,6 @@
 .fb5 {
   width: 10%;
   height: 33%;
-  background-color: var(--building-color2);
   position: relative;
   right: 10%;
   background: repeating-linear-gradient(
@@ -275,5 +274,6 @@
   width: 9%;
   height: 38%;
   background-color: var(--building-color3);
-}
-
+
+}
+
```

Código completo tras este paso: `pasos/paso-103/`

## Paso 104

> Finally! You made it to the last building! Add a repeating gradient to it with a `90deg` direction. Use the building color from `0%` to `10%` and `transparent` from `10%` to `30%`.

Cambio en `styles.css`:

```diff
@@ -274,6 +274,12 @@
   width: 9%;
   height: 38%;
   background-color: var(--building-color3);
-
-}
-
+  background: repeating-linear-gradient(
+    90deg,
+    var(--building-color3),
+    var(--building-color3) 10%,
+    transparent 10%,
+    transparent 30%
+  )
+}
+
```

Código completo tras este paso: `pasos/paso-104/`

## Paso 105

> Add another repeating gradient to this building; make it the same as the one you just added, except don't add the `90deg` direction and use your window color instead of the two `transparent` colors.

Cambio en `styles.css`:

```diff
@@ -275,11 +275,17 @@
   height: 38%;
   background-color: var(--building-color3);
   background: repeating-linear-gradient(
-    90deg,
-    var(--building-color3),
-    var(--building-color3) 10%,
-    transparent 10%,
-    transparent 30%
-  )
-}
-
+      90deg,
+      var(--building-color3),
+      var(--building-color3) 10%,
+      transparent 10%,
+      transparent 30%
+    ),
+    repeating-linear-gradient(
+      var(--building-color3),
+      var(--building-color3) 10%,
+      var(--window-color3) 10%,
+      var(--window-color3) 30%
+    );
+}
+
```

Código completo tras este paso: `pasos/paso-105/`

## Paso 106

> You can remove the `background-color` for this building now, since it isn't needed.

Cambio en `styles.css`:

```diff
@@ -273,7 +273,6 @@
 .fb6 {
   width: 9%;
   height: 38%;
-  background-color: var(--building-color3);
   background: repeating-linear-gradient(
       90deg,
       var(--building-color3),
```

Código completo tras este paso: `pasos/paso-106/`

## Paso 107

> Okay, the buildings are done. Go back to the `*` selector and remove the `border` you applied to everything at the beginning and the buildings will come together.

Cambio en `styles.css`:

```diff
@@ -10,7 +10,6 @@
 }
 
 * {
-  border: 1px solid black;
   box-sizing: border-box;
 }
 
```

Código completo tras este paso: `pasos/paso-107/`

## Paso 108

> Add `sky` as a second class to the `.background-buildings` element. You are going to make a background for the skyline.

Cambio en `index.html`:

```diff
@@ -7,7 +7,7 @@
   </head>
 
   <body>
-    <div class="background-buildings">
+    <div class="background-buildings sky">
       <div></div>
       <div></div>
       <div class="bb1 building-wrap">
```

Cambio en `styles.css`:

```diff
@@ -40,6 +40,8 @@
   align-items: center;
   justify-content: space-evenly;
 }
+
+
 
 /* BACKGROUND BUILDINGS - "bb" stands for "background building" */
 .bb1 {
```

Código completo tras este paso: `pasos/paso-108/`

## Paso 109

> Give the `sky` class a `radial-gradient`. Use `#ffcf33` from `0%` to `20%`, `#ffff66` at `21%`, and `#bbeeff` at `100%`. This will add circular gradient to the background that will be your sun.

Cambio en `styles.css`:

```diff
@@ -41,7 +41,14 @@
   justify-content: space-evenly;
 }
 
-
+.sky {
+  background: radial-gradient(
+      #ffcf33,
+      #ffcf33 20%,
+      #ffff66 21%,
+      #bbeeff 100%
+    );
+}
 
 /* BACKGROUND BUILDINGS - "bb" stands for "background building" */
 .bb1 {
```

Código completo tras este paso: `pasos/paso-109/`

## Paso 110

> At the top of the sky gradient color list, where you would put a direction for the gradient; add `circle closest-corner at 15% 15%,`. This will move the start of the gradient to `15%` from the top and left. It will make it end at the `closest-corner` and it will maintain a `circle` shape. These are some keywords built into gradients to describe how it behaves.

Cambio en `styles.css`:

```diff
@@ -43,6 +43,7 @@
 
 .sky {
   background: radial-gradient(
+      closest-corner circle at 15% 15%,
       #ffcf33,
       #ffcf33 20%,
       #ffff66 21%,
```

Código completo tras este paso: `pasos/paso-110/`

## Paso 111

> In the previous module you learned that media queries can be used to change styles based on certain conditions, and they look like this:
> 
> ```css
> @media (condition) {
> 
> }  
> ```
> 
> Add an empty media query at the bottom of your stylesheet with a condition of `max-width: 1000px`. Styles added in here will take effect when the document size is 1000px wide or less.

Cambio en `styles.css`:

```diff
@@ -297,3 +297,7 @@
     );
 }
 
+@media (max-width: 1000px) {
+
+}
+
```

Código completo tras este paso: `pasos/paso-111/`

## Paso 112

> Copy and paste your whole `sky` class along with all of its properties and values into the media query. You are going to make another color scheme for the skyline that changes it from day to night.
> 
> Note: You are going to need to scroll past the editable region to copy the class.

Cambio en `styles.css`:

```diff
@@ -43,11 +43,11 @@
 
 .sky {
   background: radial-gradient(
-      closest-corner circle at 15% 15%,
-      #ffcf33,
-      #ffcf33 20%,
-      #ffff66 21%,
-      #bbeeff 100%
+closest-corner circle at 15% 15%,
+#ffcf33,
+#ffcf33 20%,
+#ffff66 21%,
+#bbeeff 100%
     );
 }
 
@@ -112,7 +112,7 @@
   width: 10%;
   height: 55%;
   background: repeating-linear-gradient(
-      90deg,
+90deg,
       var(--building-color3),
       var(--building-color3),
       var(--window-color3) 15%
@@ -170,11 +170,11 @@
   width: 100%;
   height: 80%;
   background: repeating-linear-gradient(
-      90deg,
+90deg,
       var(--building-color4),
       var(--building-color4) 10%,
-      transparent 10%,
-      transparent 15%
+transparent 10%,
+transparent 15%
     ),
     repeating-linear-gradient(
       var(--building-color4),
@@ -267,11 +267,11 @@
   background: repeating-linear-gradient(
       var(--building-color2),
       var(--building-color2) 5%,
-      transparent 5%,
-      transparent 10%
+transparent 5%,
+transparent 10%
     ),
     repeating-linear-gradient(
-      90deg,
+90deg,
       var(--building-color2),
       var(--building-color2) 12%,
       var(--window-color2) 12%,
@@ -283,11 +283,11 @@
   width: 9%;
   height: 38%;
   background: repeating-linear-gradient(
-      90deg,
+90deg,
       var(--building-color3),
       var(--building-color3) 10%,
-      transparent 10%,
-      transparent 30%
+transparent 10%,
+transparent 30%
     ),
     repeating-linear-gradient(
       var(--building-color3),
@@ -298,6 +298,14 @@
 }
 
 @media (max-width: 1000px) {
-
-}
-
+  .sky {
+    background: radial-gradient(
+  closest-corner circle at 15% 15%,
+  #ffcf33,
+  #ffcf33 20%,
+  #ffff66 21%,
+  #bbeeff 100%
+);
+  }
+}
+
```

Código completo tras este paso: `pasos/paso-112/`

## Paso 113

> In the `sky` class of the media query, change the two `#ffcf33` color values to `#ccc`, the `#ffff66` to `#445`, and the `#bbeeff` to `#223`. Then you can resize your window to see the background change colors.

Cambio en `styles.css`:

```diff
@@ -43,11 +43,11 @@
 
 .sky {
   background: radial-gradient(
-closest-corner circle at 15% 15%,
-#ffcf33,
-#ffcf33 20%,
-#ffff66 21%,
-#bbeeff 100%
+      closest-corner circle at 15% 15%,
+      #ffcf33,
+      #ffcf33 20%,
+      #ffff66 21%,
+      #bbeeff 100%
     );
 }
 
@@ -112,7 +112,7 @@
   width: 10%;
   height: 55%;
   background: repeating-linear-gradient(
-90deg,
+      90deg,
       var(--building-color3),
       var(--building-color3),
       var(--window-color3) 15%
@@ -170,11 +170,11 @@
   width: 100%;
   height: 80%;
   background: repeating-linear-gradient(
-90deg,
+      90deg,
       var(--building-color4),
       var(--building-color4) 10%,
-transparent 10%,
-transparent 15%
+      transparent 10%,
+      transparent 15%
     ),
     repeating-linear-gradient(
       var(--building-color4),
@@ -267,11 +267,11 @@
   background: repeating-linear-gradient(
       var(--building-color2),
       var(--building-color2) 5%,
-transparent 5%,
-transparent 10%
+      transparent 5%,
+      transparent 10%
     ),
     repeating-linear-gradient(
-90deg,
+      90deg,
       var(--building-color2),
       var(--building-color2) 12%,
       var(--window-color2) 12%,
@@ -283,11 +283,11 @@
   width: 9%;
   height: 38%;
   background: repeating-linear-gradient(
-90deg,
+      90deg,
       var(--building-color3),
       var(--building-color3) 10%,
-transparent 10%,
-transparent 30%
+      transparent 10%,
+      transparent 30%
     ),
     repeating-linear-gradient(
       var(--building-color3),
@@ -298,14 +298,16 @@
 }
 
 @media (max-width: 1000px) {
+
+
   .sky {
     background: radial-gradient(
-  closest-corner circle at 15% 15%,
-  #ffcf33,
-  #ffcf33 20%,
-  #ffff66 21%,
-  #bbeeff 100%
-);
+        closest-corner circle at 15% 15%,
+        #ccc,
+        #ccc 20%,
+        #445 21%,
+        #223 100%
+      );
   }
 }
 
```

Código completo tras este paso: `pasos/paso-113/`

## Paso 114

> Add a `:root` selector to the top of your media query. Then redefine all four of the `--building-color` variables to use the value `#000` there.

Cambio en `styles.css`:

```diff
@@ -298,7 +298,13 @@
 }
 
 @media (max-width: 1000px) {
-
+  :root {
+    --building-color1: #000;
+    --building-color2: #000;
+    --building-color3: #000;
+    --building-color4: #000;
+
+  }
 
   .sky {
     background: radial-gradient(
```

Código completo tras este paso: `pasos/paso-114/`

## Paso 115

> Lastly, in the `:root` selector of the media query, redefine all four of the `--window-color` variables to use `#777`. When you're done, resize the window and watch it go from day to night.
> 
> Variables are primarily used with colors, and that's how you used them here. But they can be given any value and used on any property. Your project looks great!

Cambio en `styles.css`:

```diff
@@ -303,7 +303,10 @@
     --building-color2: #000;
     --building-color3: #000;
     --building-color4: #000;
-
+    --window-color1: #777;
+    --window-color2: #777;
+    --window-color3: #777;
+    --window-color4: #777;
   }
 
   .sky {
```

Código completo tras este paso: `pasos/paso-115/`
