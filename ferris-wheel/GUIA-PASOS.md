# Ferris Wheel (CSS Animation) — solución paso a paso

Código completo de cada paso en `pasos/paso-NNN/`.

## Paso 1

> To start, add a `link` element for the `./styles.css` file.

Cambio en `index.html`:

```diff
@@ -3,7 +3,7 @@
   <head>
     <meta charset="UTF-8">
     <title>Ferris Wheel</title>
-
+    <link rel="stylesheet" href="./styles.css">
   </head>
   <body>
 
```

Código completo tras este paso: `pasos/paso-001/`

## Paso 2

> Add a `div` within your `body` element and give it a `class` of `wheel`.
> 
> Inside your new `div`, add six `span` elements with a `class` set to `line`, and six `div` elements with a `class` set to `cabin`.

Cambio en `index.html`:

```diff
@@ -6,7 +6,21 @@
     <link rel="stylesheet" href="./styles.css">
   </head>
   <body>
+    <div class="wheel">
+      <span class="line"></span>
+      <span class="line"></span>
+      <span class="line"></span>
+      <span class="line"></span>
+      <span class="line"></span>
+      <span class="line"></span>
 
+      <div class="cabin"></div>
+      <div class="cabin"></div>
+      <div class="cabin"></div>
+      <div class="cabin"></div>
+      <div class="cabin"></div>
+      <div class="cabin"></div>
+    </div>
   </body>
 </html>
 
```

Código completo tras este paso: `pasos/paso-002/`

## Paso 3

> Create a selector for your `.wheel` element. Start by setting the `border` to `2px solid black`, the `border-radius` to `50%`, and the `margin-left` to `50px`.

Cambio en `styles.css`:

```diff
@@ -1,2 +1,7 @@
+.wheel {
+  border: 2px solid black;
+  border-radius: 50%;
+  margin-left: 50px;
 
+}
 
```

Código completo tras este paso: `pasos/paso-003/`

## Paso 4

> Set the `position` property of the `.wheel` selector to `absolute`. Set the `height` and `width` both to `55vw`.

Cambio en `styles.css`:

```diff
@@ -2,6 +2,9 @@
   border: 2px solid black;
   border-radius: 50%;
   margin-left: 50px;
+  position: absolute;
+  height: 55vw;
+  width: 55vw;
 
 }
 
```

Código completo tras este paso: `pasos/paso-004/`

## Paso 5

> Give your `.wheel` selector a `max-height` and `max-width` property both set to `500px`.

Cambio en `styles.css`:

```diff
@@ -5,6 +5,7 @@
   position: absolute;
   height: 55vw;
   width: 55vw;
-
+  max-width: 500px;
+  max-height: 500px;
 }
 
```

Código completo tras este paso: `pasos/paso-005/`

## Paso 6

> Create a selector for your `.line` elements. Start by setting the `background-color` to `black`, the `width` to `50%`, and the `height` to `2px`.

Cambio en `styles.css`:

```diff
@@ -9,3 +9,10 @@
   max-height: 500px;
 }
 
+.line {
+  background-color: black;
+  width: 50%;
+  height: 2px;
+
+}
+
```

Código completo tras este paso: `pasos/paso-006/`

## Paso 7

> Set the `.line` selector's `position` property to `absolute`, the `left` property to `50%`, and the `top` property to `50%`.

Cambio en `styles.css`:

```diff
@@ -13,6 +13,9 @@
   background-color: black;
   width: 50%;
   height: 2px;
+  position: absolute;
+  top: 50%;
+  left: 50%;
 
 }
 
```

Código completo tras este paso: `pasos/paso-007/`

## Paso 8

> The `transform-origin` property is used to set the point around which a CSS transformation is applied. For example, when you apply a `rotate` transformation (as you'll do later in this project), the `transform-origin` determines around which point the element is rotated.
> 
> Give the `.line` selector a `transform-origin` property of `0% 0%`. This will offset the origin point at `0%` from the left and `0%` from the top, setting it to the top left corner of the element.

Cambio en `styles.css`:

```diff
@@ -16,6 +16,6 @@
   position: absolute;
   top: 50%;
   left: 50%;
-
+  transform-origin: 0% 0%;
 }
 
```

Código completo tras este paso: `pasos/paso-008/`

## Paso 9

> Create a selector to target your second `.line` element. Set the `transform` property to `rotate(60deg)`.
> 
> Remember that the `transform` property allows you to manipulate the shape of an element. In this case, using the `rotate(60deg)` value will rotate the element around its `transform-origin` point by 60 degrees clockwise.

Cambio en `styles.css`:

```diff
@@ -19,3 +19,7 @@
   transform-origin: 0% 0%;
 }
 
+.line:nth-of-type(2) {
+  transform: rotate(60deg);
+}
+
```

Código completo tras este paso: `pasos/paso-009/`

## Paso 10

> Using the same pattern, create a separate selector for the third `.line`, the fourth `.line`, the fifth `.line`, and the sixth `.line`.
> 
> Set the `transform` property for the third `.line` to `rotate(120deg)`, the fourth to `rotate(180deg)`, the fifth to `rotate(240deg)`, and the sixth to `rotate(300deg)`.

Cambio en `styles.css`:

```diff
@@ -22,4 +22,16 @@
 .line:nth-of-type(2) {
   transform: rotate(60deg);
 }
+.line:nth-of-type(3) {
+  transform: rotate(120deg);
+}
+.line:nth-of-type(4) {
+  transform: rotate(180deg);
+}
+.line:nth-of-type(5) {
+  transform: rotate(240deg);
+}
+.line:nth-of-type(6) {
+  transform: rotate(300deg);
+}
 
```

Código completo tras este paso: `pasos/paso-010/`

## Paso 11

> Create a `.cabin` selector. Set the `background-color` to `red`, the `width` to `20%`, and the `height` to `20%`.

Cambio en `styles.css`:

```diff
@@ -35,3 +35,10 @@
   transform: rotate(300deg);
 }
 
+.cabin {
+  background-color: red;
+  width: 20%;
+  height: 20%;
+
+}
+
```

Código completo tras este paso: `pasos/paso-011/`

## Paso 12

> Give the `.cabin` a `position` of `absolute`, and a `border` of `2px solid`.

Cambio en `styles.css`:

```diff
@@ -39,6 +39,8 @@
   background-color: red;
   width: 20%;
   height: 20%;
+  position: absolute;
+  border: 2px solid;
 
 }
 
```

Código completo tras este paso: `pasos/paso-012/`

## Paso 13

> Set the `.cabin` to have a `transform-origin` property of `50% 0%`. This will set the origin point to be offset `50%` from the left and `0%` from the top, placing it in the middle of the top edge of the element.

Cambio en `styles.css`:

```diff
@@ -41,6 +41,6 @@
   height: 20%;
   position: absolute;
   border: 2px solid;
-
+  transform-origin: 50% 0%;
 }
 
```

Código completo tras este paso: `pasos/paso-013/`

## Paso 14

> Time to position the cabins around the wheel. Select the first `.cabin` element. Set the `right` property to `-8.5%` and the `top` property to `50%`.

Cambio en `styles.css`:

```diff
@@ -44,3 +44,8 @@
   transform-origin: 50% 0%;
 }
 
+.cabin:nth-of-type(1) {
+  right: -8.5%;
+  top: 50%;
+}
+
```

Código completo tras este paso: `pasos/paso-014/`

## Paso 15

> Continuing the pattern, select the following `.cabin` elements and apply the specific rules to them:
> 
> - The second `.cabin` should have the `right` property set to `17%` and the `top` property set to `93.5%`.
> - The third `.cabin` should have the `right` property set to `67%` and the `top` property set to `93.5%`.
> - The fourth `.cabin` should have the `left` property set to `-8.5%` and the `top` property set to `50%`.
> - The fifth `.cabin` should have the `left` property set to `17%` and the `top` property set to `7%`.
> - The sixth `.cabin` should have the `right` property set to `17%` and the `top` property set to `7%`.

Cambio en `styles.css`:

```diff
@@ -48,4 +48,24 @@
   right: -8.5%;
   top: 50%;
 }
+.cabin:nth-of-type(2) {
+  right: 17%;
+  top: 93.5%;
+}
+.cabin:nth-of-type(3) {
+  right: 67%;
+  top: 93.5%;
+}
+.cabin:nth-of-type(4) {
+  left: -8.5%;
+  top: 50%;
+}
+.cabin:nth-of-type(5) {
+  left: 17%;
+  top: 7%;
+}
+.cabin:nth-of-type(6) {
+  right: 17%;
+  top: 7%;
+}
 
```

Código completo tras este paso: `pasos/paso-015/`

## Paso 16

> The `@keyframes` at-rule is used to define the flow of a CSS animation. Within the `@keyframes` rule, you can create selectors for specific points in the animation sequence, such as `0%` or `25%`, or use `from` and `to` to define the start and end of the sequence.
> 
> `@keyframes` rules require a name to be assigned to them, which you use in other rules to reference. For example, the `@keyframes freeCodeCamp { }` rule would be named `freeCodeCamp`.
> 
> Time to start animating. Create a `@keyframes` rule named `wheel`.

Cambio en `styles.css`:

```diff
@@ -69,3 +69,7 @@
   top: 7%;
 }
 
+@keyframes wheel {
+
+}
+
```

Código completo tras este paso: `pasos/paso-016/`

## Paso 17

> You now need to define how your animation should start. To do this, create a `0%` rule within your `@keyframes wheel` rule. The properties you set in this nested selector will apply at the beginning of your animation.
> 
> As an example, this would be a `12%` rule:
> 
> ```css
> @keyframes freecodecamp {
>   12% {
>     color: green;
>   }
> }
> ```

Cambio en `styles.css`:

```diff
@@ -70,6 +70,8 @@
 }
 
 @keyframes wheel {
+  0% {
 
+  }
 }
 
```

Código completo tras este paso: `pasos/paso-017/`

## Paso 18

> Give the `0%` rule a `transform` property set to `rotate(0deg)`. This will start the animation with no rotation.

Cambio en `styles.css`:

```diff
@@ -71,7 +71,8 @@
 
 @keyframes wheel {
   0% {
+    transform: rotate(0deg);
+  }
 
-  }
 }
 
```

Código completo tras este paso: `pasos/paso-018/`

## Paso 19

> Now give the `@keyframes wheel` rule a `100%` selector. Within that, set the `transform` to `rotate(360deg)`. By doing this, your animation will now complete a full rotation.

Cambio en `styles.css`:

```diff
@@ -7,6 +7,7 @@
   width: 55vw;
   max-width: 500px;
   max-height: 500px;
+
 }
 
 .line {
@@ -73,6 +74,8 @@
   0% {
     transform: rotate(0deg);
   }
-
+  100% {
+    transform: rotate(360deg);
+  }
 }
 
```

Código completo tras este paso: `pasos/paso-019/`

## Paso 20

> The `animation-name` property is used to link a `@keyframes` rule to a CSS selector. The value of this property should match the name of the `@keyframes` rule. Give your `.wheel` selector an `animation-name` property set to `wheel`.
> 
> The `animation-duration` property is used to set how long the animation should sequence to complete. The time should be specified in either seconds (`s`) or milliseconds (`ms`). Set your `.wheel` selector to have an `animation-duration` property of `10s`.

Cambio en `styles.css`:

```diff
@@ -7,6 +7,8 @@
   width: 55vw;
   max-width: 500px;
   max-height: 500px;
+  animation-name: wheel;
+  animation-duration: 10s;
 
 }
 
```

Código completo tras este paso: `pasos/paso-020/`

## Paso 21

> The `animation-iteration-count` property sets how many times your animation should repeat. This can be set to a number, or to `infinite` to indefinitely repeat the animation. Your Ferris wheel should never stop, so set the `.wheel` selector to have an `animation-iteration-count` of `infinite`.
> 
> The `animation-timing-function` property sets how the animation should progress over time. There are a few different values for this property, but you want the Ferris wheel animation to run at the same rate from start to finish. Set the `animation-timing-function` to `linear` in your `.wheel` selector.

Cambio en `styles.css`:

```diff
@@ -9,7 +9,8 @@
   max-height: 500px;
   animation-name: wheel;
   animation-duration: 10s;
-
+  animation-iteration-count: infinite;
+  animation-timing-function: linear;
 }
 
 .line {
```

Código completo tras este paso: `pasos/paso-021/`

## Paso 22

> Create another `@keyframes` rule with the name `cabins`. Use the same properties as your `@keyframes wheel`, copying both the `0%` and `100%` rules, but set the `transform` property of the `100%` selector to `rotate(-360deg)`.

Cambio en `styles.css`:

```diff
@@ -46,6 +46,7 @@
   position: absolute;
   border: 2px solid;
   transform-origin: 50% 0%;
+
 }
 
 .cabin:nth-of-type(1) {
@@ -82,3 +83,12 @@
   }
 }
 
+@keyframes cabins {
+  0% {
+    transform: rotate(0deg);
+  }
+  100% {
+    transform: rotate(-360deg);
+  }
+}
+
```

Código completo tras este paso: `pasos/paso-022/`

## Paso 23

> With your `.wheel` selector, you created four different properties to control the animation. For your `.cabin` selector, you can use the `animation` property to set these all at once.
> 
> Set the `animation` property of the `.cabin` rule to `cabins 10s linear infinite`. This will set the `animation-name`, `animation-duration`, `animation-timing-function`, and `animation-iteration-count` properties in that order.

Cambio en `styles.css`:

```diff
@@ -46,7 +46,7 @@
   position: absolute;
   border: 2px solid;
   transform-origin: 50% 0%;
-
+  animation: cabins 10s linear infinite;
 }
 
 .cabin:nth-of-type(1) {
```

Código completo tras este paso: `pasos/paso-023/`

## Paso 24

> To make your cabin animation seem more like a natural swinging motion, you can use the `ease-in-out` timing function. This setting will tell the animation to start and end at a slower pace, but move more quickly in the middle of the cycle.
> 
> Replace `linear` to `ease-in-out` in the `.cabin` selector.

Cambio en `styles.css`:

```diff
@@ -46,7 +46,7 @@
   position: absolute;
   border: 2px solid;
   transform-origin: 50% 0%;
-  animation: cabins 10s linear infinite;
+  animation: cabins 10s ease-in-out infinite;
 }
 
 .cabin:nth-of-type(1) {
@@ -86,6 +86,7 @@
 @keyframes cabins {
   0% {
     transform: rotate(0deg);
+
   }
   100% {
     transform: rotate(-360deg);
```

Código completo tras este paso: `pasos/paso-024/`

## Paso 25

> You can use `@keyframes` rules to control more than just the transformation of an element. In the `0%` selector of your `@keyframes cabins`, set the `background-color` to `yellow`.

Cambio en `styles.css`:

```diff
@@ -86,8 +86,9 @@
 @keyframes cabins {
   0% {
     transform: rotate(0deg);
+    background-color: yellow;
+  }
 
-  }
   100% {
     transform: rotate(-360deg);
   }
```

Código completo tras este paso: `pasos/paso-025/`

## Paso 26

> Between the `0%` and `100%` selectors, add a `50%` selector. This will apply in the middle of the animation cycle. Set the `background-color` to `purple`.

Cambio en `styles.css`:

```diff
@@ -88,7 +88,9 @@
     transform: rotate(0deg);
     background-color: yellow;
   }
-
+  50% {
+    background-color: purple;
+  }
   100% {
     transform: rotate(-360deg);
   }
```

Código completo tras este paso: `pasos/paso-026/`

## Paso 27

> Because the animation is on an infinite loop and the start and end colors are not the same, the transition appears jerky when it switches back to yellow from red. 
> 
> To start fixing this, remove the `background-color` from your `0%` selector.

Cambio en `styles.css`:

```diff
@@ -86,8 +86,8 @@
 @keyframes cabins {
   0% {
     transform: rotate(0deg);
-    background-color: yellow;
   }
+
   50% {
     background-color: purple;
   }
```

Código completo tras este paso: `pasos/paso-027/`

## Paso 28

> Create a new `25%` selector between your `0%` and `50%` selectors. Give this new selector the `background-color` property set to `yellow`.

Cambio en `styles.css`:

```diff
@@ -87,10 +87,13 @@
   0% {
     transform: rotate(0deg);
   }
-
+  25% {
+    background-color: yellow;
+  }
   50% {
     background-color: purple;
   }
+
   100% {
     transform: rotate(-360deg);
   }
```

Código completo tras este paso: `pasos/paso-028/`

## Paso 29

> Finally, create a new `75%` selector between your `50%` and `100%` selectors. Give this new selector a `background-color` property set to `yellow`.
> 
> With that, your animation is much smoother and your Ferris wheel is complete.

Código completo tras este paso: `pasos/paso-029/`
