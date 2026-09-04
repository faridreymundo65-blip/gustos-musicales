# Flappy Penguin (CSS Transforms) — solución paso a paso

Código completo de cada paso en `pasos/paso-NNN/`.

## Paso 1

> You will be building a happy Flappy Penguin, and further practicing CSS transforms and animations in the process.
> 
> Begin with linking your stylesheet to the page.

Cambio en `index.html`:

```diff
@@ -2,7 +2,7 @@
 <html lang="en">
   <head>
     <meta charset="UTF-8" />
-
+    <link rel="stylesheet" href="./styles.css" />
     <title>Penguin</title>
     <meta name="viewport" content="width=device-width, initial-scale=1.0" />
   </head>
```

Código completo tras este paso: `pasos/paso-001/`

## Paso 2

> Target the `body` element to set the `background` to a linear gradient angled 45 degrees clockwise, starting at `rgb(118, 201, 255)` and ending at `rgb(247, 255, 222)`.

Cambio en `styles.css`:

```diff
@@ -1,2 +1,5 @@
+body {
+  background: linear-gradient(45deg, rgb(118, 201, 255), rgb(247, 255, 222));
 
+}
 
```

Código completo tras este paso: `pasos/paso-002/`

## Paso 3

> Normalize your page's sizing, by removing the `body` element's `margin` and `padding`.

Cambio en `styles.css`:

```diff
@@ -1,5 +1,7 @@
 body {
   background: linear-gradient(45deg, rgb(118, 201, 255), rgb(247, 255, 222));
+  margin: 0;
+  padding: 0;
 
 }
 
```

Código completo tras este paso: `pasos/paso-003/`

## Paso 4

> Normalize your page, by setting the `width` to `100%`, and `height` to `100vh`.

Cambio en `styles.css`:

```diff
@@ -2,6 +2,8 @@
   background: linear-gradient(45deg, rgb(118, 201, 255), rgb(247, 255, 222));
   margin: 0;
   padding: 0;
+  width: 100%;
+  height: 100vh;
 
 }
 
```

Código completo tras este paso: `pasos/paso-004/`

## Paso 5

> Remove both the horizontal and vertical scrollbars, using only one property.

Cambio en `index.html`:

```diff
@@ -8,6 +8,7 @@
   </head>
 
   <body>
+
   </body>
 </html>
 
```

Cambio en `styles.css`:

```diff
@@ -4,6 +4,6 @@
   padding: 0;
   width: 100%;
   height: 100vh;
-
+  overflow: hidden;
 }
 
```

Código completo tras este paso: `pasos/paso-005/`

## Paso 6

> Within the `body`, add a `div` with a `class` of `ground`.

Cambio en `index.html`:

```diff
@@ -8,7 +8,7 @@
   </head>
 
   <body>
-
+    <div class="ground"></div>
   </body>
 </html>
 
```

Código completo tras este paso: `pasos/paso-006/`

## Paso 7

> Target the `.ground` element, and set its `width` to take up the full width of the viewport. Then, set the `height` to `400px`.

Cambio en `styles.css`:

```diff
@@ -7,3 +7,9 @@
   overflow: hidden;
 }
 
+.ground {
+  width: 100vw;
+  height: 400px;
+
+}
+
```

Código completo tras este paso: `pasos/paso-007/`

## Paso 8

> Give the `.ground` element a `background` with a linear gradient angled 90 degrees clockwise, starting at `rgb(88, 175, 236)` and ending at `rgb(182, 255, 255)`.

Cambio en `styles.css`:

```diff
@@ -10,6 +10,7 @@
 .ground {
   width: 100vw;
   height: 400px;
+  background: linear-gradient(90deg, rgb(88, 175, 236), rgb(182, 255, 255));
 
 }
 
```

Código completo tras este paso: `pasos/paso-008/`

## Paso 9

> As the `.ground` element will be third in the stacking context of the page layout, set its `z-index` to `3`, and `position` to `absolute`.

Cambio en `index.html`:

```diff
@@ -8,6 +8,8 @@
   </head>
 
   <body>
+
+
     <div class="ground"></div>
   </body>
 </html>
```

Cambio en `styles.css`:

```diff
@@ -11,6 +11,7 @@
   width: 100vw;
   height: 400px;
   background: linear-gradient(90deg, rgb(88, 175, 236), rgb(182, 255, 255));
-
+  z-index: 3;
+  position: absolute;
 }
 
```

Código completo tras este paso: `pasos/paso-009/`

## Paso 10

> Above the `.ground` element, add a `div` with a `class` of `penguin`. This `div` will contain Flappy Penguin.

Cambio en `index.html`:

```diff
@@ -8,7 +8,7 @@
   </head>
 
   <body>
-
+    <div class="penguin"></div>
 
     <div class="ground"></div>
   </body>
```

Cambio en `styles.css`:

```diff
@@ -7,6 +7,8 @@
   overflow: hidden;
 }
 
+
+
 .ground {
   width: 100vw;
   height: 400px;
```

Código completo tras este paso: `pasos/paso-010/`

## Paso 11

> Target the `.penguin` element, and set its `width` and `height` to `300px`.

Cambio en `styles.css`:

```diff
@@ -7,7 +7,11 @@
   overflow: hidden;
 }
 
+.penguin {
+  width: 300px;
+  height: 300px;
 
+}
 
 .ground {
   width: 100vw;
```

Código completo tras este paso: `pasos/paso-011/`

## Paso 12

> Use the `margin` property to horizontally center the `.penguin` element, and set the `margin-top` to `75px`.

Cambio en `index.html`:

```diff
@@ -8,6 +8,7 @@
   </head>
 
   <body>
+
     <div class="penguin"></div>
 
     <div class="ground"></div>
```

Cambio en `styles.css`:

```diff
@@ -10,7 +10,8 @@
 .penguin {
   width: 300px;
   height: 300px;
-
+  margin: auto;
+  margin-top: 75px;
 }
 
 .ground {
```

Código completo tras este paso: `pasos/paso-012/`

## Paso 13

> To create some scenery in the background, you will add two mountains.
> 
> Above the `.penguin` element, add a `div` with a `class` of `left-mountain`.

Cambio en `index.html`:

```diff
@@ -8,7 +8,7 @@
   </head>
 
   <body>
-
+    <div class="left-mountain"></div>
     <div class="penguin"></div>
 
     <div class="ground"></div>
```

Cambio en `styles.css`:

```diff
@@ -6,6 +6,8 @@
   height: 100vh;
   overflow: hidden;
 }
+
+
 
 .penguin {
   width: 300px;
```

Código completo tras este paso: `pasos/paso-013/`

## Paso 14

> Target the `.left-mountain` element, and set its `width` and `height` to `300px`. Then, set the `background` to a linear gradient starting at `rgb(203, 241, 228)` and ending at `rgb(80, 183, 255)`.

Cambio en `styles.css`:

```diff
@@ -7,7 +7,12 @@
   overflow: hidden;
 }
 
+.left-mountain {
+  width: 300px;
+  height: 300px;
+  background: linear-gradient(rgb(203, 241, 228), rgb(80, 183, 255));
 
+}
 
 .penguin {
   width: 300px;
```

Código completo tras este paso: `pasos/paso-014/`

## Paso 15

> To prevent the mountain from pushing the `.ground` element, adjust its `position` to prevent it from taking up space in the page layout.

Cambio en `styles.css`:

```diff
@@ -11,6 +11,7 @@
   width: 300px;
   height: 300px;
   background: linear-gradient(rgb(203, 241, 228), rgb(80, 183, 255));
+  position: absolute;
 
 }
 
```

Código completo tras este paso: `pasos/paso-015/`

## Paso 16

> To make the mountain look more like a mountain, you can use the `skew` transform function, which takes two arguments. The first being an angle to shear the x-axis by, and the second being an angle to shear the y-axis by.
> 
> Use the `transform` property to skew the mountain by `0deg` in the x-axis and `44deg` in the y-axis.

Cambio en `styles.css`:

```diff
@@ -12,6 +12,7 @@
   height: 300px;
   background: linear-gradient(rgb(203, 241, 228), rgb(80, 183, 255));
   position: absolute;
+  transform: skew(0deg, 44deg);
 
 }
 
```

Código completo tras este paso: `pasos/paso-016/`

## Paso 17

> Set the stack level of the mountain element such that it remains directly behind the `.ground` element.

Cambio en `styles.css`:

```diff
@@ -13,6 +13,7 @@
   background: linear-gradient(rgb(203, 241, 228), rgb(80, 183, 255));
   position: absolute;
   transform: skew(0deg, 44deg);
+  z-index: 2;
 
 }
 
@@ -29,5 +30,6 @@
   background: linear-gradient(90deg, rgb(88, 175, 236), rgb(182, 255, 255));
   z-index: 3;
   position: absolute;
+
 }
 
```

Código completo tras este paso: `pasos/paso-017/`

## Paso 18

> To overlap the mountain and `.ground` elements better, give the mountain a `margin-top` of `100px`, and the `.ground` element a `margin-top` of `-58px`.

Cambio en `index.html`:

```diff
@@ -9,6 +9,7 @@
 
   <body>
     <div class="left-mountain"></div>
+
     <div class="penguin"></div>
 
     <div class="ground"></div>
```

Cambio en `styles.css`:

```diff
@@ -14,7 +14,7 @@
   position: absolute;
   transform: skew(0deg, 44deg);
   z-index: 2;
-
+  margin-top: 100px;
 }
 
 .penguin {
@@ -30,6 +30,6 @@
   background: linear-gradient(90deg, rgb(88, 175, 236), rgb(182, 255, 255));
   z-index: 3;
   position: absolute;
-
+  margin-top: -58px;
 }
 
```

Código completo tras este paso: `pasos/paso-018/`

## Paso 19

> To give the effect of a mountain range, add another mountain, by creating a new `div` immediately after `.left-mountain`, and give the new `div` the `class` of `back-mountain`.

Cambio en `index.html`:

```diff
@@ -9,7 +9,7 @@
 
   <body>
     <div class="left-mountain"></div>
-
+    <div class="back-mountain"></div>
     <div class="penguin"></div>
 
     <div class="ground"></div>
```

Cambio en `styles.css`:

```diff
@@ -17,6 +17,8 @@
   margin-top: 100px;
 }
 
+
+
 .penguin {
   width: 300px;
   height: 300px;
```

Código completo tras este paso: `pasos/paso-019/`

## Paso 20

> Target the `.back-mountain` element, and set its `width` and `height` to `300px`. Then, set the `background` to a linear gradient starting at `rgb(203, 241, 228)` and ending at `rgb(47, 170, 255)`.

Cambio en `styles.css`:

```diff
@@ -17,7 +17,12 @@
   margin-top: 100px;
 }
 
+.back-mountain {
+  width: 300px;
+  height: 300px;
+  background: linear-gradient(rgb(203, 241, 228), rgb(47, 170, 255));
 
+}
 
 .penguin {
   width: 300px;
```

Código completo tras este paso: `pasos/paso-020/`

## Paso 21

> Set the `position` property of the `.back-mountain` to prevent it from taking up space in the page layout.

Cambio en `styles.css`:

```diff
@@ -21,6 +21,7 @@
   width: 300px;
   height: 300px;
   background: linear-gradient(rgb(203, 241, 228), rgb(47, 170, 255));
+  position: absolute;
 
 }
 
```

Código completo tras este paso: `pasos/paso-021/`

## Paso 22

> Change the stack level of the `.back-mountain` element such that it is directly behind the `.left-mountain` element.

Cambio en `styles.css`:

```diff
@@ -22,6 +22,7 @@
   height: 300px;
   background: linear-gradient(rgb(203, 241, 228), rgb(47, 170, 255));
   position: absolute;
+  z-index: 1;
 
 }
 
```

Código completo tras este paso: `pasos/paso-022/`

## Paso 23

> Rotate the `.back-mountain` element by `45deg` clockwise. Then, give it a `left` property of `110px`, and a `top` property of `225px`.

Cambio en `index.html`:

```diff
@@ -10,6 +10,7 @@
   <body>
     <div class="left-mountain"></div>
     <div class="back-mountain"></div>
+
     <div class="penguin"></div>
 
     <div class="ground"></div>
```

Cambio en `styles.css`:

```diff
@@ -23,7 +23,9 @@
   background: linear-gradient(rgb(203, 241, 228), rgb(47, 170, 255));
   position: absolute;
   z-index: 1;
-
+  transform: rotate(45deg);
+  left: 110px;
+  top: 225px;
 }
 
 .penguin {
```

Código completo tras este paso: `pasos/paso-023/`

## Paso 24

> To finish the background, add a sun, by creating a new `div` element immediately after the `.back-mountain` element, and give it the class of `sun`.

Cambio en `index.html`:

```diff
@@ -10,7 +10,7 @@
   <body>
     <div class="left-mountain"></div>
     <div class="back-mountain"></div>
-
+    <div class="sun"></div>
     <div class="penguin"></div>
 
     <div class="ground"></div>
```

Cambio en `styles.css`:

```diff
@@ -28,6 +28,8 @@
   top: 225px;
 }
 
+
+
 .penguin {
   width: 300px;
   height: 300px;
```

Código completo tras este paso: `pasos/paso-024/`

## Paso 25

> Give the `.sun` element a `width` and `height` of `200px`, and a `background-color` of `yellow`.

Cambio en `styles.css`:

```diff
@@ -28,7 +28,12 @@
   top: 225px;
 }
 
+.sun {
+  width: 200px;
+  height: 200px;
+  background-color: yellow;
 
+}
 
 .penguin {
   width: 300px;
```

Código completo tras este paso: `pasos/paso-025/`

## Paso 26

> Set the `position` property of the sun to prevent it from taking up space in the page layout, and set the `border-radius` such that the sun's shape is a circle.

Cambio en `styles.css`:

```diff
@@ -32,6 +32,8 @@
   width: 200px;
   height: 200px;
   background-color: yellow;
+  position: absolute;
+  border-radius: 50%;
 
 }
 
```

Código completo tras este paso: `pasos/paso-026/`

## Paso 27

> Position the sun in the top right corner of the screen such that `75px` of its top and right edges are off screen.

Cambio en `index.html`:

```diff
@@ -11,7 +11,9 @@
     <div class="left-mountain"></div>
     <div class="back-mountain"></div>
     <div class="sun"></div>
-    <div class="penguin"></div>
+    <div class="penguin">
+
+    </div>
 
     <div class="ground"></div>
   </body>
```

Cambio en `styles.css`:

```diff
@@ -34,7 +34,8 @@
   background-color: yellow;
   position: absolute;
   border-radius: 50%;
-
+  top: -75px;
+  right: -75px;
 }
 
 .penguin {
```

Código completo tras este paso: `pasos/paso-027/`

## Paso 28

> Your penguin will consist of two main sections: the head, and the body.
> 
> Within `.penguin`, add two new `div` elements. The first with a `class` of `penguin-head`, and the second with a `class` of `penguin-body`.

Cambio en `index.html`:

```diff
@@ -12,7 +12,8 @@
     <div class="back-mountain"></div>
     <div class="sun"></div>
     <div class="penguin">
-
+      <div class="penguin-head"></div>
+      <div class="penguin-body"></div>
     </div>
 
     <div class="ground"></div>
```

Cambio en `styles.css`:

```diff
@@ -43,6 +43,7 @@
   height: 300px;
   margin: auto;
   margin-top: 75px;
+
 }
 
 .ground {
```

Código completo tras este paso: `pasos/paso-028/`

## Paso 29

> Change the stack level of the `.penguin` element such that it appears in front of the `.ground` element, and give it a `position` of `relative`.

Cambio en `styles.css`:

```diff
@@ -43,8 +43,11 @@
   height: 300px;
   margin: auto;
   margin-top: 75px;
+  z-index: 4;
+  position: relative;
+}
 
-}
+
 
 .ground {
   width: 100vw;
```

Código completo tras este paso: `pasos/paso-029/`

## Paso 30

> Target the `.penguin-head` element, and give it a `width` half of its parent's, and a `height` of `45%`. Then, set the `background` to a linear gradient at `45deg` starting at `gray`, and ending at `rgb(239, 240, 228)`.

Cambio en `styles.css`:

```diff
@@ -47,7 +47,16 @@
   position: relative;
 }
 
+.penguin-head {
+  width: 50%;
+  height: 45%;
+  background: linear-gradient(
+    45deg,
+    gray,
+    rgb(239, 240, 228)
+  );
 
+}
 
 .ground {
   width: 100vw;
```

Código completo tras este paso: `pasos/paso-030/`

## Paso 31

> _Most_ penguins do not have a square head.
> 
> Give the penguin a slightly oval head by setting the radius of the top corners to `70%` and the radius of the bottom corners to `65%`.

Cambio en `styles.css`:

```diff
@@ -55,8 +55,10 @@
     gray,
     rgb(239, 240, 228)
   );
+  border-radius: 70% 70% 65% 65%;
+}
 
-}
+
 
 .ground {
   width: 100vw;
```

Código completo tras este paso: `pasos/paso-031/`

## Paso 32

> Target the `.penguin-body` element, and give it a `width` of `53%`, and a `height` of `45%`. Then, set the `background` to a linear gradient at `45deg`, `rgb(134, 133, 133)` from `0%`, `rgb(234, 231, 231)` from `25%`, and `white` from `67%`.

Cambio en `styles.css`:

```diff
@@ -58,7 +58,17 @@
   border-radius: 70% 70% 65% 65%;
 }
 
+.penguin-body {
+  width: 53%;
+  height: 45%;
+  background: linear-gradient(
+    45deg,
+    rgb(134, 133, 133) 0%,
+    rgb(234, 231, 231) 25%,
+    white 67%
+  );
 
+}
 
 .ground {
   width: 100vw;
```

Código completo tras este paso: `pasos/paso-032/`

## Paso 33

> Another interesting fact about penguins is that they do not have square bodies.
> 
> Use the `border-radius` property with a value of `80% 80% 100% 100%`, to give the penguin a slightly rounded body.

Cambio en `styles.css`:

```diff
@@ -47,6 +47,8 @@
   position: relative;
 }
 
+
+
 .penguin-head {
   width: 50%;
   height: 45%;
@@ -67,7 +69,7 @@
     rgb(234, 231, 231) 25%,
     white 67%
   );
-
+  border-radius: 80% 80% 100% 100%;
 }
 
 .ground {
```

Código completo tras este paso: `pasos/paso-033/`

## Paso 34

> Target all descendent elements of the `.penguin` element, and give them a `position` of `absolute`.

Cambio en `styles.css`:

```diff
@@ -47,7 +47,9 @@
   position: relative;
 }
 
-
+.penguin * {
+  position: absolute;
+}
 
 .penguin-head {
   width: 50%;
@@ -58,6 +60,7 @@
     rgb(239, 240, 228)
   );
   border-radius: 70% 70% 65% 65%;
+
 }
 
 .penguin-body {
```

Código completo tras este paso: `pasos/paso-034/`

## Paso 35

> Position the `.penguin-head` element `10%` from the top, and `25%` from the left of its parent.

Cambio en `styles.css`:

```diff
@@ -60,7 +60,8 @@
     rgb(239, 240, 228)
   );
   border-radius: 70% 70% 65% 65%;
-
+  top: 10%;
+  left: 25%;
 }
 
 .penguin-body {
@@ -73,6 +74,7 @@
     white 67%
   );
   border-radius: 80% 80% 100% 100%;
+
 }
 
 .ground {
```

Código completo tras este paso: `pasos/paso-035/`

## Paso 36

> Position the `.penguin-body` element `40%` from the top, and `23.5%` from the left of its parent.

Cambio en `styles.css`:

```diff
@@ -62,6 +62,7 @@
   border-radius: 70% 70% 65% 65%;
   top: 10%;
   left: 25%;
+
 }
 
 .penguin-body {
@@ -74,7 +75,8 @@
     white 67%
   );
   border-radius: 80% 80% 100% 100%;
-
+  top: 40%;
+  left: 23.5%;
 }
 
 .ground {
```

Código completo tras este paso: `pasos/paso-036/`

## Paso 37

> Change the stack level of the `.penguin-head` element such that it appears in front of the `.penguin-body` element.

Cambio en `styles.css`:

```diff
@@ -62,7 +62,7 @@
   border-radius: 70% 70% 65% 65%;
   top: 10%;
   left: 25%;
-
+  z-index: 1;
 }
 
 .penguin-body {
@@ -79,6 +79,8 @@
   left: 23.5%;
 }
 
+
+
 .ground {
   width: 100vw;
   height: 400px;
```

Código completo tras este paso: `pasos/paso-037/`

## Paso 38

> To give the penguin body a crest, create a pseudo-element that is the first child of the `.penguin-body` element. Set the `content` property of the pseudo-element to an empty string.

Cambio en `styles.css`:

```diff
@@ -79,7 +79,10 @@
   left: 23.5%;
 }
 
+.penguin-body::before {
+  content: "";
 
+}
 
 .ground {
   width: 100vw;
```

Código completo tras este paso: `pasos/paso-038/`

## Paso 39

> Position the pseudo-element relative to its closest positioned ancestor.

Cambio en `styles.css`:

```diff
@@ -81,6 +81,7 @@
 
 .penguin-body::before {
   content: "";
+  position: absolute;
 
 }
 
```

Código completo tras este paso: `pasos/paso-039/`

## Paso 40

> Give the pseudo-element a `width` half that of its parent, a `height` of `45%`, and a `background-color` of `gray`.

Cambio en `styles.css`:

```diff
@@ -82,6 +82,9 @@
 .penguin-body::before {
   content: "";
   position: absolute;
+  width: 50%;
+  height: 45%;
+  background-color: gray;
 
 }
 
```

Código completo tras este paso: `pasos/paso-040/`

## Paso 41

> Position the pseudo-element `10%` from the top and `25%` from the left of its parent.

Cambio en `styles.css`:

```diff
@@ -85,6 +85,8 @@
   width: 50%;
   height: 45%;
   background-color: gray;
+  top: 10%;
+  left: 25%;
 
 }
 
```

Código completo tras este paso: `pasos/paso-041/`

## Paso 42

> Round off the crest, by giving the pseudo-element bottom corners a radius of `100%`, leaving the top corners at `0%`.

Cambio en `styles.css`:

```diff
@@ -87,6 +87,7 @@
   background-color: gray;
   top: 10%;
   left: 25%;
+  border-radius: 0% 0% 100% 100%;
 
 }
 
```

Código completo tras este paso: `pasos/paso-042/`

## Paso 43

> Increase the pseudo-element's transparency by `30%`.

Cambio en `index.html`:

```diff
@@ -12,7 +12,9 @@
     <div class="back-mountain"></div>
     <div class="sun"></div>
     <div class="penguin">
-      <div class="penguin-head"></div>
+      <div class="penguin-head">
+
+      </div>
       <div class="penguin-body"></div>
     </div>
 
```

Cambio en `styles.css`:

```diff
@@ -88,7 +88,7 @@
   top: 10%;
   left: 25%;
   border-radius: 0% 0% 100% 100%;
-
+  opacity: 70%;
 }
 
 .ground {
```

Código completo tras este paso: `pasos/paso-043/`

## Paso 44

> Start the penguin's face, by adding two `div` elements within `.penguin-head`, and giving them both a `class` of `face`.

Cambio en `index.html`:

```diff
@@ -13,7 +13,8 @@
     <div class="sun"></div>
     <div class="penguin">
       <div class="penguin-head">
-
+        <div class="face"></div>
+        <div class="face"></div>
       </div>
       <div class="penguin-body"></div>
     </div>
```

Cambio en `styles.css`:

```diff
@@ -65,6 +65,8 @@
   z-index: 1;
 }
 
+
+
 .penguin-body {
   width: 53%;
   height: 45%;
```

Código completo tras este paso: `pasos/paso-044/`

## Paso 45

> Give the `.face` elements a `width` of `60%`, a `height` of `70%`, and a `background-color` of `white`.

Cambio en `styles.css`:

```diff
@@ -65,7 +65,12 @@
   z-index: 1;
 }
 
+.face {
+  width: 60%;
+  height: 70%;
+  background-color: white;
 
+}
 
 .penguin-body {
   width: 53%;
```

Código completo tras este paso: `pasos/paso-045/`

## Paso 46

> Make the top corners of the `.face` elements have a radius of `70%`, and the bottom corners have a radius of `60%`.

Cambio en `styles.css`:

```diff
@@ -69,6 +69,7 @@
   width: 60%;
   height: 70%;
   background-color: white;
+  border-radius: 70% 70% 60% 60%;
 
 }
 
```

Código completo tras este paso: `pasos/paso-046/`

## Paso 47

> Position the `.face` elements so that they are `15%` from the top.

Cambio en `styles.css`:

```diff
@@ -70,7 +70,7 @@
   height: 70%;
   background-color: white;
   border-radius: 70% 70% 60% 60%;
-
+  top: 15%;
 }
 
 .penguin-body {
```

Código completo tras este paso: `pasos/paso-047/`

## Paso 48

> Currently, the two `.face` elements are on top of each other.
> 
> Fix this, by adding a `class` of `left` to the first `.face` element, and a `class` of `right` to the second `.face` element.

Cambio en `index.html`:

```diff
@@ -13,8 +13,8 @@
     <div class="sun"></div>
     <div class="penguin">
       <div class="penguin-head">
-        <div class="face"></div>
-        <div class="face"></div>
+        <div class="face left"></div>
+        <div class="face right"></div>
       </div>
       <div class="penguin-body"></div>
     </div>
```

Cambio en `styles.css`:

```diff
@@ -73,6 +73,8 @@
   top: 15%;
 }
 
+
+
 .penguin-body {
   width: 53%;
   height: 45%;
```

Código completo tras este paso: `pasos/paso-048/`

## Paso 49

> Target the `.face` element with the `left` class, and position it `5%` left of its parent.

Cambio en `styles.css`:

```diff
@@ -73,6 +73,10 @@
   top: 15%;
 }
 
+.face.left {
+  left: 5%;
+}
+
 
 
 .penguin-body {
```

Código completo tras este paso: `pasos/paso-049/`

## Paso 50

> Target the `.face` element with the `right` class, and position it `5%` right of its parent.

Cambio en `index.html`:

```diff
@@ -15,6 +15,7 @@
       <div class="penguin-head">
         <div class="face left"></div>
         <div class="face right"></div>
+
       </div>
       <div class="penguin-body"></div>
     </div>
```

Cambio en `styles.css`:

```diff
@@ -77,7 +77,9 @@
   left: 5%;
 }
 
-
+.face.right {
+  right: 5%;
+}
 
 .penguin-body {
   width: 53%;
```

Código completo tras este paso: `pasos/paso-050/`

## Paso 51

> Below the `.face.right` element, add a `div` element with a `class` of `chin`.

Cambio en `index.html`:

```diff
@@ -15,7 +15,7 @@
       <div class="penguin-head">
         <div class="face left"></div>
         <div class="face right"></div>
-
+        <div class="chin"></div>
       </div>
       <div class="penguin-body"></div>
     </div>
```

Cambio en `styles.css`:

```diff
@@ -81,6 +81,8 @@
   right: 5%;
 }
 
+
+
 .penguin-body {
   width: 53%;
   height: 45%;
```

Código completo tras este paso: `pasos/paso-051/`

## Paso 52

> Target the `.chin` element, and give it a `width` of `90%`, `height` of `70%`, and `background-color` of `white`.

Cambio en `styles.css`:

```diff
@@ -81,7 +81,12 @@
   right: 5%;
 }
 
+.chin {
+  width: 90%;
+  height: 70%;
+  background-color: white;
 
+}
 
 .penguin-body {
   width: 53%;
```

Código completo tras este paso: `pasos/paso-052/`

## Paso 53

> Position the `.chin` element such that it is `25%` from the top, and `5%` from the left of its parent. Then, give the top corners a radius of `70%`, and the bottom corners a radius of `100%`.

Cambio en `styles.css`:

```diff
@@ -1,3 +1,5 @@
+
+
 body {
   background: linear-gradient(45deg, rgb(118, 201, 255), rgb(247, 255, 222));
   margin: 0;
@@ -85,7 +87,9 @@
   width: 90%;
   height: 70%;
   background-color: white;
-
+  top: 25%;
+  left: 5%;
+  border-radius: 70% 70% 100% 100%;
 }
 
 .penguin-body {
```

Código completo tras este paso: `pasos/paso-053/`

## Paso 54

> So far, the `.face` and `.chin` elements have the same `background-color`.
> 
> Create a custom CSS property called `--penguin-face`, and set it to `white`.

Cambio en `styles.css`:

```diff
@@ -1,4 +1,6 @@
-
+:root {
+  --penguin-face: white;
+}
 
 body {
   background: linear-gradient(45deg, rgb(118, 201, 255), rgb(247, 255, 222));
```

Código completo tras este paso: `pasos/paso-054/`

## Paso 55

> Where relevant, replace property values with your `--penguin-face` variable.

Cambio en `index.html`:

```diff
@@ -16,6 +16,7 @@
         <div class="face left"></div>
         <div class="face right"></div>
         <div class="chin"></div>
+
       </div>
       <div class="penguin-body"></div>
     </div>
```

Cambio en `styles.css`:

```diff
@@ -72,7 +72,7 @@
 .face {
   width: 60%;
   height: 70%;
-  background-color: white;
+  background-color: var(--penguin-face);
   border-radius: 70% 70% 60% 60%;
   top: 15%;
 }
@@ -88,7 +88,7 @@
 .chin {
   width: 90%;
   height: 70%;
-  background-color: white;
+  background-color: var(--penguin-face);
   top: 25%;
   left: 5%;
   border-radius: 70% 70% 100% 100%;
```

Código completo tras este paso: `pasos/paso-055/`

## Paso 56

> Below the `.chin` element, add two `div` elements each with a `class` of `eye`. Also, give the first `.eye` element a `class` of `left`, and the second `.eye` element a `class` of `right`.

Cambio en `index.html`:

```diff
@@ -16,7 +16,8 @@
         <div class="face left"></div>
         <div class="face right"></div>
         <div class="chin"></div>
-
+        <div class="eye left"></div>
+        <div class="eye right"></div>
       </div>
       <div class="penguin-body"></div>
     </div>
```

Cambio en `styles.css`:

```diff
@@ -94,6 +94,8 @@
   border-radius: 70% 70% 100% 100%;
 }
 
+
+
 .penguin-body {
   width: 53%;
   height: 45%;
```

Código completo tras este paso: `pasos/paso-056/`

## Paso 57

> Target the `.eye` elements, and give them a `width` of `15%`, `height` of `17%`, and `background-color` of `black`.

Cambio en `styles.css`:

```diff
@@ -94,7 +94,12 @@
   border-radius: 70% 70% 100% 100%;
 }
 
+.eye {
+  width: 15%;
+  height: 17%;
+  background-color: black;
 
+}
 
 .penguin-body {
   width: 53%;
```

Código completo tras este paso: `pasos/paso-057/`

## Paso 58

> Position the `.eye` elements `45%` from the top of their parent, and give all corners a radius of `50%`.

Cambio en `styles.css`:

```diff
@@ -98,8 +98,11 @@
   width: 15%;
   height: 17%;
   background-color: black;
+  top: 45%;
+  border-radius: 50%;
+}
 
-}
+
 
 .penguin-body {
   width: 53%;
```

Código completo tras este paso: `pasos/paso-058/`

## Paso 59

> Target the `.eye` element with the `left` class, and position it `25%` from the left of its parent. Then, target the `.eye` element with the `right` class, and position it `25%` from the right of its parent.

Cambio en `index.html`:

```diff
@@ -16,8 +16,12 @@
         <div class="face left"></div>
         <div class="face right"></div>
         <div class="chin"></div>
-        <div class="eye left"></div>
-        <div class="eye right"></div>
+        <div class="eye left">
+
+        </div>
+        <div class="eye right">
+
+        </div>
       </div>
       <div class="penguin-body"></div>
     </div>
```

Cambio en `styles.css`:

```diff
@@ -102,7 +102,13 @@
   border-radius: 50%;
 }
 
+.eye.left {
+  left: 25%;
+}
 
+.eye.right {
+  right: 25%;
+}
 
 .penguin-body {
   width: 53%;
```

Código completo tras este paso: `pasos/paso-059/`

## Paso 60

> Within each `.eye` element, add a `div` with a `class` of `eye-lid`.

Cambio en `index.html`:

```diff
@@ -17,10 +17,10 @@
         <div class="face right"></div>
         <div class="chin"></div>
         <div class="eye left">
-
+          <div class="eye-lid"></div>
         </div>
         <div class="eye right">
-
+          <div class="eye-lid"></div>
         </div>
       </div>
       <div class="penguin-body"></div>
```

Cambio en `styles.css`:

```diff
@@ -110,6 +110,8 @@
   right: 25%;
 }
 
+
+
 .penguin-body {
   width: 53%;
   height: 45%;
```

Código completo tras este paso: `pasos/paso-060/`

## Paso 61

> Target the `.eye-lid` elements, and give them a `width` of `150%`, `height` of `100%`, and `background-color` of `--penguin-face`.

Cambio en `styles.css`:

```diff
@@ -110,7 +110,12 @@
   right: 25%;
 }
 
+.eye-lid {
+  width: 150%;
+  height: 100%;
+  background-color: var(--penguin-face);
 
+}
 
 .penguin-body {
   width: 53%;
```

Código completo tras este paso: `pasos/paso-061/`

## Paso 62

> Position the `.eye-lid` elements `25%` from the top, and `-23%` from the left of their parents. Then, give all corners a radius of `50%`.

Cambio en `index.html`:

```diff
@@ -22,6 +22,7 @@
         <div class="eye right">
           <div class="eye-lid"></div>
         </div>
+
       </div>
       <div class="penguin-body"></div>
     </div>
```

Cambio en `styles.css`:

```diff
@@ -114,7 +114,9 @@
   width: 150%;
   height: 100%;
   background-color: var(--penguin-face);
-
+  top: 25%;
+  left: -23%;
+  border-radius: 50%;
 }
 
 .penguin-body {
```

Código completo tras este paso: `pasos/paso-062/`

## Paso 63

> Below the `.eye.right` element, add two `div` elements each with a `class` of `blush`. Also, give the first `.blush` element a `class` of `left`, and the second `.blush` element a `class` of `right`.

Cambio en `index.html`:

```diff
@@ -22,7 +22,8 @@
         <div class="eye right">
           <div class="eye-lid"></div>
         </div>
-
+        <div class="blush left"></div>
+        <div class="blush right"></div>
       </div>
       <div class="penguin-body"></div>
     </div>
```

Cambio en `styles.css`:

```diff
@@ -119,6 +119,8 @@
   border-radius: 50%;
 }
 
+
+
 .penguin-body {
   width: 53%;
   height: 45%;
```

Código completo tras este paso: `pasos/paso-063/`

## Paso 64

> Target the `.blush` elements, and give them a `width` of `15%`, `height` of `10%`, and `background-color` of `pink`.

Cambio en `styles.css`:

```diff
@@ -119,7 +119,12 @@
   border-radius: 50%;
 }
 
+.blush {
+  width: 15%;
+  height: 10%;
+  background-color: pink;
 
+}
 
 .penguin-body {
   width: 53%;
```

Código completo tras este paso: `pasos/paso-064/`

## Paso 65

> Position the `.blush` elements `65%` from the top of their parent, and give all corners a radius of `50%`.

Cambio en `styles.css`:

```diff
@@ -123,8 +123,11 @@
   width: 15%;
   height: 10%;
   background-color: pink;
+  top: 65%;
+  border-radius: 50%;
+}
 
-}
+
 
 .penguin-body {
   width: 53%;
```

Código completo tras este paso: `pasos/paso-065/`

## Paso 66

> Target the `.blush` element with a `class` of `left`, and position it `15%` left of its parent. Then, target the `.blush` element with a `class` of `right`, and position it `15%` right of its parent.

Cambio en `index.html`:

```diff
@@ -24,6 +24,7 @@
         </div>
         <div class="blush left"></div>
         <div class="blush right"></div>
+
       </div>
       <div class="penguin-body"></div>
     </div>
```

Cambio en `styles.css`:

```diff
@@ -127,7 +127,13 @@
   border-radius: 50%;
 }
 
+.blush.left {
+  left: 15%;
+}
 
+.blush.right {
+  right: 15%;
+}
 
 .penguin-body {
   width: 53%;
```

Código completo tras este paso: `pasos/paso-066/`

## Paso 67

> Below the `.blush.right` element, add two `div` elements each with a `class` of `beak`. Also, give the first `.beak` element a `class` of `top`, and the second `.beak` element a `class` of `bottom`.

Cambio en `index.html`:

```diff
@@ -24,7 +24,8 @@
         </div>
         <div class="blush left"></div>
         <div class="blush right"></div>
-
+        <div class="beak top"></div>
+        <div class="beak bottom"></div>
       </div>
       <div class="penguin-body"></div>
     </div>
```

Cambio en `styles.css`:

```diff
@@ -135,6 +135,8 @@
   right: 15%;
 }
 
+
+
 .penguin-body {
   width: 53%;
   height: 45%;
```

Código completo tras este paso: `pasos/paso-067/`

## Paso 68

> Target the `.beak` elements, and give them a `height` of `10%`, `background-color` of `orange`, and give all corners a radius of `50%`.

Cambio en `styles.css`:

```diff
@@ -135,6 +135,12 @@
   right: 15%;
 }
 
+.beak {
+  height: 10%;
+  background-color: orange;
+  border-radius: 50%;
+}
+
 
 
 .penguin-body {
```

Código completo tras este paso: `pasos/paso-068/`

## Paso 69

> Target the `.beak` element with a `class` of `top`, give it a `width` of `20%`, and position it `60%` from the top, and `40%` from the left of its parent.

Cambio en `styles.css`:

```diff
@@ -141,6 +141,12 @@
   border-radius: 50%;
 }
 
+.beak.top {
+  width: 20%;
+  top: 60%;
+  left: 40%;
+}
+
 
 
 .penguin-body {
```

Código completo tras este paso: `pasos/paso-069/`

## Paso 70

> Target the `.beak` element with a `class` of `bottom`, and give it a `width` that's `4%` smaller than `.beak.top`, `5%` further from the top, and `2%` further from the left of its parent than `.beak.top`.

Cambio en `index.html`:

```diff
@@ -27,6 +27,7 @@
         <div class="beak top"></div>
         <div class="beak bottom"></div>
       </div>
+
       <div class="penguin-body"></div>
     </div>
 
```

Cambio en `styles.css`:

```diff
@@ -147,7 +147,11 @@
   left: 40%;
 }
 
-
+.beak.bottom {
+  width: 16%;
+  top: 65%;
+  left: 42%;
+}
 
 .penguin-body {
   width: 53%;
```

Código completo tras este paso: `pasos/paso-070/`

## Paso 71

> The penguin's body looks a bit plain. Spruce him up by adding a `div` element with a `class` of `shirt`, immediately before the `.penguin-body` element.

Cambio en `index.html`:

```diff
@@ -27,7 +27,9 @@
         <div class="beak top"></div>
         <div class="beak bottom"></div>
       </div>
+      <div class="shirt">
 
+      </div>
       <div class="penguin-body"></div>
     </div>
 
```

Código completo tras este paso: `pasos/paso-071/`

## Paso 72

> Within the `.shirt` element, add a `div` with the following emoji as content: 💜

Cambio en `index.html`:

```diff
@@ -28,6 +28,7 @@
         <div class="beak bottom"></div>
       </div>
       <div class="shirt">
+        <div>💜</div>
 
       </div>
       <div class="penguin-body"></div>
```

Código completo tras este paso: `pasos/paso-072/`

## Paso 73

> Within `.shirt`, after the `div` element, add a `p` element with the following content: `I CSS`

Cambio en `index.html`:

```diff
@@ -29,7 +29,7 @@
       </div>
       <div class="shirt">
         <div>💜</div>
-
+        <p>I CSS</p>
       </div>
       <div class="penguin-body"></div>
     </div>
```

Cambio en `styles.css`:

```diff
@@ -153,6 +153,8 @@
   left: 42%;
 }
 
+
+
 .penguin-body {
   width: 53%;
   height: 45%;
```

Código completo tras este paso: `pasos/paso-073/`

## Paso 74

> Target the `.shirt` element, and set its `font-size` to `25px`, `font-family` to `Helvetica` with a fallback of `sans-serif`, and `font-weight` to `bold`.

Cambio en `styles.css`:

```diff
@@ -153,6 +153,10 @@
   left: 42%;
 }
 
+.shirt {
+  font: bold 25px Helvetica, sans-serif;
+}
+
 
 
 .penguin-body {
```

Código completo tras este paso: `pasos/paso-074/`

## Paso 75

> In some browsers, the _heart_ emoji may look slightly different from the previous step. This is because some of the character's properties were overridden by the `font-weight` style of `bold`.
> 
> Fix this, by targeting the `div` with the heart emoji, and setting its `font-weight` to its original value.

Cambio en `styles.css`:

```diff
@@ -157,7 +157,10 @@
   font: bold 25px Helvetica, sans-serif;
 }
 
+.shirt div {
+  font-weight: initial;
 
+}
 
 .penguin-body {
   width: 53%;
```

Código completo tras este paso: `pasos/paso-075/`

## Paso 76

> Position the `div` with the heart emoji `22.5px` from the top, and `12px` from the left of its parent.

Cambio en `styles.css`:

```diff
@@ -155,11 +155,13 @@
 
 .shirt {
   font: bold 25px Helvetica, sans-serif;
+
 }
 
 .shirt div {
   font-weight: initial;
-
+  top: 22.5px;
+  left: 12px;
 }
 
 .penguin-body {
```

Código completo tras este paso: `pasos/paso-076/`

## Paso 77

> Position the `.shirt` element `165px` from the top, and `127.5px` from the left of its parent. Then, increase its stacking order such that it appears above the `.penguin-body` element.

Cambio en `styles.css`:

```diff
@@ -155,6 +155,9 @@
 
 .shirt {
   font: bold 25px Helvetica, sans-serif;
+  top: 165px;
+  left: 127.5px;
+  z-index: 1;
 
 }
 
```

Código completo tras este paso: `pasos/paso-077/`

## Paso 78

> For the shirt's final touch, set the `color` to `#6a6969`.

Cambio en `index.html`:

```diff
@@ -31,7 +31,9 @@
         <div>💜</div>
         <p>I CSS</p>
       </div>
-      <div class="penguin-body"></div>
+      <div class="penguin-body">
+
+      </div>
     </div>
 
     <div class="ground"></div>
```

Cambio en `styles.css`:

```diff
@@ -158,7 +158,7 @@
   top: 165px;
   left: 127.5px;
   z-index: 1;
-
+  color: #6a6969;
 }
 
 .shirt div {
```

Código completo tras este paso: `pasos/paso-078/`

## Paso 79

> Fun fact: Penguins cannot stand without at least two feet.
> 
> Within the `.penguin-body` element, add two `div` elements each with a `class` of `foot`. Give the first `.foot` a `class` of `left`, and the second `.foot` a `class` of `right`.

Cambio en `index.html`:

```diff
@@ -32,7 +32,8 @@
         <p>I CSS</p>
       </div>
       <div class="penguin-body">
-
+        <div class="foot left"></div>
+        <div class="foot right"></div>
       </div>
     </div>
 
```

Cambio en `styles.css`:

```diff
@@ -193,6 +193,8 @@
   opacity: 70%;
 }
 
+
+
 .ground {
   width: 100vw;
   height: 400px;
```

Código completo tras este paso: `pasos/paso-079/`

## Paso 80

> Target the `.foot` elements, and give them a `width` of `15%`, `height` of `30%`, and `background-color` of `orange`.

Cambio en `styles.css`:

```diff
@@ -193,7 +193,12 @@
   opacity: 70%;
 }
 
-
+.foot {
+  width: 15%;
+  height: 30%;
+  background-color: orange;
+
+}
 
 .ground {
   width: 100vw;
```

Código completo tras este paso: `pasos/paso-080/`

## Paso 81

> Position the `.foot` elements `85%` from the top of their parent, and give all corners a radius of `50%`.

Cambio en `styles.css`:

```diff
@@ -1,5 +1,6 @@
 :root {
   --penguin-face: white;
+
 }
 
 body {
@@ -197,7 +198,8 @@
   width: 15%;
   height: 30%;
   background-color: orange;
-
+  top: 85%;
+  border-radius: 50%;
 }
 
 .ground {
```

Código completo tras este paso: `pasos/paso-081/`

## Paso 82

> The penguin's beak and feet share the same `color`.
> 
> Create a new custom CSS variable named `--penguin-picorna`, and replace all relevant property values with it.

Cambio en `styles.css`:

```diff
@@ -1,6 +1,6 @@
 :root {
   --penguin-face: white;
-
+  --penguin-picorna: orange;
 }
 
 body {
@@ -138,7 +138,7 @@
 
 .beak {
   height: 10%;
-  background-color: orange;
+  background-color: var(--penguin-picorna);
   border-radius: 50%;
 }
 
@@ -197,10 +197,12 @@
 .foot {
   width: 15%;
   height: 30%;
-  background-color: orange;
+  background-color: var(--penguin-picorna);
   top: 85%;
   border-radius: 50%;
 }
+
+
 
 .ground {
   width: 100vw;
```

Código completo tras este paso: `pasos/paso-082/`

## Paso 83

> Target the `.foot` element with a `class` of `left`, and position it `25%` left of its parent. Then, target the `.foot` element with a `class` of `right`, and position it `25%` right of its parent.

Cambio en `styles.css`:

```diff
@@ -202,7 +202,15 @@
   border-radius: 50%;
 }
 
-
+.foot.left {
+  left: 25%;
+
+}
+
+.foot.right {
+  right: 25%;
+
+}
 
 .ground {
   width: 100vw;
```

Código completo tras este paso: `pasos/paso-083/`

## Paso 84

> To make the penguin's feet look more _penguiny_, rotate the left foot by `80deg`, and the right by `-80deg`.

Cambio en `styles.css`:

```diff
@@ -200,16 +200,17 @@
   background-color: var(--penguin-picorna);
   top: 85%;
   border-radius: 50%;
+
 }
 
 .foot.left {
   left: 25%;
-
+  transform: rotate(80deg);
 }
 
 .foot.right {
   right: 25%;
-
+  transform: rotate(-80deg);
 }
 
 .ground {
```

Código completo tras este paso: `pasos/paso-084/`

## Paso 85

> Change the stacking order of the `.foot` elements such that they appear beneath the `.penguin-body` element.

Cambio en `index.html`:

```diff
@@ -32,6 +32,7 @@
         <p>I CSS</p>
       </div>
       <div class="penguin-body">
+
         <div class="foot left"></div>
         <div class="foot right"></div>
       </div>
```

Cambio en `styles.css`:

```diff
@@ -200,7 +200,7 @@
   background-color: var(--penguin-picorna);
   top: 85%;
   border-radius: 50%;
-
+  z-index: -1;
 }
 
 .foot.left {
```

Código completo tras este paso: `pasos/paso-085/`

## Paso 86

> Fun fact: Penguins cannot fly without wings.
> 
> Within `.penguin-body`, before the `.foot` elements, add two `div` elements each with a `class` of `arm`. Give the first `.arm` a `class` of `left`, and the second `.arm` a `class` of `right`.

Cambio en `index.html`:

```diff
@@ -32,7 +32,8 @@
         <p>I CSS</p>
       </div>
       <div class="penguin-body">
-
+        <div class="arm left"></div>
+        <div class="arm right"></div>
         <div class="foot left"></div>
         <div class="foot right"></div>
       </div>
```

Cambio en `styles.css`:

```diff
@@ -194,6 +194,8 @@
   opacity: 70%;
 }
 
+
+
 .foot {
   width: 15%;
   height: 30%;
```

Código completo tras este paso: `pasos/paso-086/`

## Paso 87

> Target the `.arm` elements, and give them a `width` of `30%`, a `height` of `60%`, and a `background` of linear gradient at `90deg` from clockwise, starting at `gray`, and ending at `rgb(209, 210, 199)`.

Cambio en `styles.css`:

```diff
@@ -1,6 +1,7 @@
 :root {
   --penguin-face: white;
   --penguin-picorna: orange;
+
 }
 
 body {
@@ -194,7 +195,15 @@
   opacity: 70%;
 }
 
-
+.arm {
+  width: 30%;
+  height: 60%;
+  background: linear-gradient(
+    90deg,
+    gray,
+    rgb(209, 210, 199)
+  );
+}
 
 .foot {
   width: 15%;
```

Código completo tras este paso: `pasos/paso-087/`

## Paso 88

> Create a custom CSS variable named `--penguin-skin`, and set it to `gray`. Then, replace all relevant property values with it.

Cambio en `styles.css`:

```diff
@@ -1,7 +1,7 @@
 :root {
   --penguin-face: white;
   --penguin-picorna: orange;
-
+  --penguin-skin: gray;
 }
 
 body {
@@ -62,7 +62,7 @@
   height: 45%;
   background: linear-gradient(
     45deg,
-    gray,
+    var(--penguin-skin),
     rgb(239, 240, 228)
   );
   border-radius: 70% 70% 65% 65%;
@@ -188,7 +188,7 @@
   position: absolute;
   width: 50%;
   height: 45%;
-  background-color: gray;
+  background-color: var(--penguin-skin);
   top: 10%;
   left: 25%;
   border-radius: 0% 0% 100% 100%;
@@ -200,10 +200,12 @@
   height: 60%;
   background: linear-gradient(
     90deg,
-    gray,
+    var(--penguin-skin),
     rgb(209, 210, 199)
   );
 }
+
+
 
 .foot {
   width: 15%;
```

Código completo tras este paso: `pasos/paso-088/`

## Paso 89

> Target the `.arm` element with a `class` of `left`, and position it `35%` from the top, and `5%` from the left of its parent. Then, target the `.arm` element with a `class` of `right`, and position it `0%` from the top, and `-5%` from the right of its parent.

Cambio en `styles.css`:

```diff
@@ -205,7 +205,16 @@
   );
 }
 
-
+.arm.left {
+  top: 35%;
+  left: 5%;
+
+}
+
+.arm.right {
+  top: 0%;
+  right: -5%;
+}
 
 .foot {
   width: 15%;
```

Código completo tras este paso: `pasos/paso-089/`

## Paso 90

> Within the `.arm.left` selector, alter the origin of the `transform` function to be the top left corner of its parent.

Cambio en `styles.css`:

```diff
@@ -208,6 +208,7 @@
 .arm.left {
   top: 35%;
   left: 5%;
+  transform-origin: top left;
 
 }
 
```

Código completo tras este paso: `pasos/paso-090/`

## Paso 91

> To keep the linear gradient on the correct side of the penguin's left arm, first rotate it by `130deg`, then invert the x-axis.

Cambio en `styles.css`:

```diff
@@ -209,12 +209,13 @@
   top: 35%;
   left: 5%;
   transform-origin: top left;
-
+  transform: rotate(130deg) scaleX(-1);
 }
 
 .arm.right {
   top: 0%;
   right: -5%;
+
 }
 
 .foot {
```

Código completo tras este paso: `pasos/paso-091/`

## Paso 92

> Rotate the right arm by `45deg` counterclockwise.

Cambio en `styles.css`:

```diff
@@ -203,6 +203,7 @@
     var(--penguin-skin),
     rgb(209, 210, 199)
   );
+
 }
 
 .arm.left {
@@ -215,7 +216,7 @@
 .arm.right {
   top: 0%;
   right: -5%;
-
+  transform: rotate(-45deg);
 }
 
 .foot {
```

Código completo tras este paso: `pasos/paso-092/`

## Paso 93

> Fun fact: Most, if not all, flippers are not naturally rectangles.
> 
> Give the `.arm` elements' top-left, top-right, and bottom-right corners a radius of `30%`, and the bottom-left corner a radius of `120%`.

Cambio en `styles.css`:

```diff
@@ -203,6 +203,7 @@
     var(--penguin-skin),
     rgb(209, 210, 199)
   );
+  border-radius: 30% 30% 30% 120%;
 
 }
 
```

Código completo tras este paso: `pasos/paso-093/`

## Paso 94

> Change the `.arm` elements' stacking order such that they appear behind the `.penguin-body` element.

Cambio en `styles.css`:

```diff
@@ -204,7 +204,7 @@
     rgb(209, 210, 199)
   );
   border-radius: 30% 30% 30% 120%;
-
+  z-index: -1;
 }
 
 .arm.left {
@@ -220,6 +220,8 @@
   transform: rotate(-45deg);
 }
 
+
+
 .foot {
   width: 15%;
   height: 30%;
```

Código completo tras este paso: `pasos/paso-094/`

## Paso 95

> Now, you are going to use CSS animations to make the penguin wave.
> 
> Define a new `@keyframes` named `wave`.

Cambio en `styles.css`:

```diff
@@ -220,7 +220,9 @@
   transform: rotate(-45deg);
 }
 
-
+@keyframes wave {
+
+}
 
 .foot {
   width: 15%;
```

Código completo tras este paso: `pasos/paso-095/`

## Paso 96

> Give `wave` four waypoints starting at `10%`, and incrementing by `10%`.

Cambio en `styles.css`:

```diff
@@ -221,7 +221,18 @@
 }
 
 @keyframes wave {
-
+  10% {
+
+  }
+  20% {
+
+  }
+  30% {
+
+  }
+  40% {
+
+  }
 }
 
 .foot {
```

Código completo tras este paso: `pasos/paso-096/`

## Paso 97

> Within the first waypoint, rotate to `110deg`, and retain the scaling of the left arm.

Cambio en `styles.css`:

```diff
@@ -222,7 +222,7 @@
 
 @keyframes wave {
   10% {
-
+    transform: rotate(110deg) scaleX(-1);
   }
   20% {
 
```

Código completo tras este paso: `pasos/paso-097/`

## Paso 98

> Within the second waypoint, rotate to `130deg`, and retain the scaling of the left arm.

Cambio en `styles.css`:

```diff
@@ -225,7 +225,7 @@
     transform: rotate(110deg) scaleX(-1);
   }
   20% {
-
+    transform: rotate(130deg) scaleX(-1);
   }
   30% {
 
```

Código completo tras este paso: `pasos/paso-098/`

## Paso 99

> For the third and fourth waypoints, repeat the `transform` pattern once more.

Cambio en `styles.css`:

```diff
@@ -212,6 +212,7 @@
   left: 5%;
   transform-origin: top left;
   transform: rotate(130deg) scaleX(-1);
+
 }
 
 .arm.right {
@@ -228,10 +229,10 @@
     transform: rotate(130deg) scaleX(-1);
   }
   30% {
-
+    transform: rotate(110deg) scaleX(-1);
   }
   40% {
-
+    transform: rotate(130deg) scaleX(-1);
   }
 }
 
```

Código completo tras este paso: `pasos/paso-099/`

## Paso 100

> Use the `wave` animation on the left arm. Have the animation last `3s`, infinitely iterate, and have a linear timing function.

Cambio en `styles.css`:

```diff
@@ -56,6 +56,8 @@
 .penguin * {
   position: absolute;
 }
+
+
 
 .penguin-head {
   width: 50%;
@@ -212,7 +214,7 @@
   left: 5%;
   transform-origin: top left;
   transform: rotate(130deg) scaleX(-1);
-
+  animation: 3s linear infinite wave;
 }
 
 .arm.right {
```

Código completo tras este paso: `pasos/paso-100/`

## Paso 101

> Target the `.penguin` element when it is active, and increase its size by `50%` in both dimensions.

Cambio en `styles.css`:

```diff
@@ -57,7 +57,10 @@
   position: absolute;
 }
 
-
+.penguin:active {
+  transform: scale(1.5);
+
+}
 
 .penguin-head {
   width: 50%;
```

Código completo tras este paso: `pasos/paso-101/`

## Paso 102

> When you activate the `.penguin` element, it might look as though you can drag it around. This is not true.
> 
> Indicate this to users, by giving the active element a `cursor` property of `not-allowed`.

Cambio en `styles.css`:

```diff
@@ -51,6 +51,7 @@
   margin-top: 75px;
   z-index: 4;
   position: relative;
+
 }
 
 .penguin * {
@@ -59,7 +60,7 @@
 
 .penguin:active {
   transform: scale(1.5);
-
+  cursor: not-allowed;
 }
 
 .penguin-head {
```

Código completo tras este paso: `pasos/paso-102/`

## Paso 103

> Change the `.penguin` element's `transition` behavior during transformation to have a duration of `1s`, a timing function of `ease-in-out`, and a delay of `0ms`.

Cambio en `styles.css`:

```diff
@@ -51,7 +51,7 @@
   margin-top: 75px;
   z-index: 4;
   position: relative;
-
+  transition: transform 1s ease-in-out 0ms;
 }
 
 .penguin * {
```

Código completo tras este paso: `pasos/paso-103/`

## Paso 104

> Finally, calculate the `height` of the `.ground` element to be the height of the viewport minus the height of the `.penguin` element.
> 
> Congratulations! You have completed the Flappy Penguin Workshop.

Código completo tras este paso: `pasos/paso-104/`
