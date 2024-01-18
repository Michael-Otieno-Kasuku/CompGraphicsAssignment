Question Nineteen
=================
Another CAD application that can be developed in WebGL is a paint program. You can
display the various objects that can be painted—lines, rectangles, circles, and triangles,
for example—and use picking to select which to draw. The mouse can then enter vertex
data and select attributes such as colors from a menu. Write such an application.

.. _webgl_paint_program:

WebGL Paint Program
===================

Introduction
------------

The WebGL Paint Program is a simple web application that allows users to draw shapes using WebGL technology. This documentation provides an overview of the HTML and JavaScript code used to implement this paint program.

HTML Structure
--------------

.. code-block:: html

   <!DOCTYPE html>
   <html lang="en">
   <head>
     <meta charset="UTF-8">
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
     <title>WebGL Paint Program</title>
     <style>
       body {
         font-family: 'Arial', sans-serif;
         display: flex;
         flex-direction: column;
         align-items: center;
         justify-content: center;
         height: 100vh;
         margin: 0;
         background-color: #f4f4f4;
       }

       canvas {
         border: 2px solid #333;
         cursor: crosshair;
         box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
         background-color: #fff;
       }

       div {
         margin-top: 20px;
         display: flex;
         align-items: center;
         justify-content: center;
       }

       label, select, input, button {
         padding: 10px;
         margin-right: 10px;
         border: 1px solid #333;
         border-radius: 4px;
         font-size: 14px;
       }

       button {
         background-color: #4caf50;
         color: white;
         cursor: pointer;
         transition: background-color 0.3s ease;
       }

       button:hover {
         background-color: #45a049;
       }
     </style>
   </head>
   <body>
     <canvas id="paintCanvas" width="800" height="600"></canvas>
     <div>
       <label for="shapeSelect">Shape:</label>
       <select id="shapeSelect">
         <option value="point">Point</option>
         <option value="line">Line</option>
         <option value="rectangle">Rectangle</option>
         <option value="circle">Circle</option>
         <option value="triangle">Triangle</option>
       </select>

       <label for="colorPicker">Color:</label>
       <input type="color" id="colorPicker" value="#ff0000">

       <button onclick="undo()">Undo</button>
     </div>

     <script>
       document.addEventListener('DOMContentLoaded', function() {
         const canvas = document.getElementById('paintCanvas');
         const gl = canvas.getContext('webgl');

         // Check for WebGL support
         if (!gl) {
           console.error('Unable to initialize WebGL. Your browser may not support it.');
           return;
         }

         const shapeSelect = document.getElementById('shapeSelect');
         const colorPicker = document.getElementById('colorPicker');

         let positions = [];
         let shapes = [];
         let currentColor = getColorFromPicker();
         let isMouseDown = false;

         canvas.addEventListener('mousedown', handleMouseDown);
         canvas.addEventListener('mousemove', handleMouseMove);
         canvas.addEventListener('mouseup', handleMouseUp);

         function handleMouseDown(event) {
           isMouseDown = true;
           const rect = canvas.getBoundingClientRect();
           const x = event.clientX - rect.left;
           const y = rect.bottom - event.clientY; // Flip y-coordinate

           positions.push(x / canvas.width * 2 - 1, y / canvas.height * 2 - 1);
           shapes.push(shapeSelect.value);
           currentColor = getColorFromPicker();
           drawScene();
         }

         function handleMouseMove(event) {
           if (isMouseDown) {
             const rect = canvas.getBoundingClientRect();
             const x = event.clientX - rect.left;
             const y = rect.bottom - event.clientY; // Flip y-coordinate
             positions.push(x / canvas.width * 2 - 1, y / canvas.height * 2 - 1);
             drawScene();
           }
         }

         function handleMouseUp() {
           isMouseDown = false;
         }

         function undo() {
           positions = positions.slice(0, -2); // Remove the last two elements (x, y)
           shapes.pop();
           drawScene();
         }

         function drawScene() {
           gl.clearColor(1.0, 1.0, 1.0, 1.0); // Clear to white
           gl.clear(gl.COLOR_BUFFER_BIT);

           for (let i = 0; i < positions.length; i += 2) {
             const shape = shapes[i / 2];
             const vertexCount = getVertexCount(shape);
             const vertices = new Float32Array(positions.slice(i, i + vertexCount * 2));

             const positionBuffer = gl.createBuffer();
             gl.bindBuffer(gl.ARRAY_BUFFER, positionBuffer);
             gl.bufferData(gl.ARRAY_BUFFER, vertices, gl.STATIC_DRAW);

             const vertexShader = createShader(gl, gl.VERTEX_SHADER, getVertexShaderSource(shape));
             const fragmentShader = createShader(gl, gl.FRAGMENT_SHADER, getFragmentShaderSource());

             const shaderProgram = createProgram(gl, vertexShader, fragmentShader);
             gl.useProgram(shaderProgram);

             const vertexPosition = gl.getAttribLocation(shaderProgram, 'aVertexPosition');
             gl.vertexAttribPointer(vertexPosition, 2, gl.FLOAT, false, 0, 0);
             gl.enableVertexAttribArray(vertexPosition);

             const uColor = gl.getUniformLocation(shaderProgram, 'uColor');
             gl.uniform4fv(uColor, currentColor);

             const uModelViewMatrix = gl.getUniformLocation(shaderProgram, 'uModelViewMatrix');
             const modelViewMatrix = new Float32Array([
               1, 0, 0, 0,
               0, 1, 0, 0,
               0, 0, 1, 0,
               0, 0, 0, 1
             ]);
             gl.uniformMatrix4fv(uModelViewMatrix, false, modelViewMatrix);

             gl.drawArrays(getDrawMode(shape), 0, vertexCount);
           }
         }

         function getVertexCount(shape) {
           switch (shape) {
             case 'point':
               return 1;
             case 'line':
               return 2;
             case 'rectangle':
               return 4;
             case 'circle':
               return 30; // Approximation with 30 vertices
             case 'triangle':
               return 3;
             default:
               return 0;
           }
         }

         function getDrawMode(shape) {
           switch (shape) {
             case 'point':
               return gl.POINTS;
             case 'line':
               return gl.LINE_STRIP;
             case 'rectangle':
             case 'circle':
             case 'triangle':
               return gl.TRIANGLE_FAN;
             default:
               return gl.POINTS;
           }
         }

         function getVertexShaderSource(shape) {
           switch (shape) {
             case 'point':
             case 'line':
               return `
                 attribute vec4 aVertexPosition;
                 uniform mat4 uModelViewMatrix;
                 void main(void) {
                   gl_Position = uModelViewMatrix * aVertexPosition;
                 }
               `;
             case 'rectangle':
             case 'circle':
             case 'triangle':
               return `
                 attribute vec4 aVertexPosition;
                 uniform mat4 uModelViewMatrix;
                 void main(void) {
                   gl_Position = uModelViewMatrix * aVertexPosition;
                 }
               `;
             default:
               return '';
           }
         }

         function getFragmentShaderSource() {
           return `
             precision mediump float;
             uniform vec4 uColor;
             void main(void) {
               gl_FragColor = uColor;
             }
           `;
         }

         function getColorFromPicker() {
           const colorHex = colorPicker.value.substring(1); // Remove the '#' character
           const r = parseInt(colorHex.substring(0, 2), 16) / 255.0;
           const g = parseInt(colorHex.substring(2, 4), 16) / 255.0;
           const b = parseInt(colorHex.substring(4, 6), 16) / 255.0;
           const a = 1.0; // Alpha value
           return [r, g, b, a];
         }

         function createShader(gl, type, source) {
           const shader = gl.createShader(type);
           gl.shaderSource(shader, source);
           gl.compileShader(shader);

           if (!gl.getShaderParameter(shader, gl.COMPILE_STATUS)) {
             console.error('An error occurred compiling the shaders: ' + gl.getShaderInfoLog(shader));
             gl.deleteShader(shader);
             return null;
           }

           return shader;
         }

         function createProgram(gl, vertexShader, fragmentShader) {
           const program = gl.createProgram();
           gl.attachShader(program, vertexShader);
           gl.attachShader(program, fragmentShader);
           gl.linkProgram(program);

           if (!gl.getProgramParameter(program, gl.LINK_STATUS)) {
             console.error('Unable to initialize the shader program: ' + gl.getProgramInfoLog(program));
             return null;
           }

           return program;
         }
       });
     </script>
   </body>
   </html>

