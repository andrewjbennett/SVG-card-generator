outer_svg = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg
   xmlns:dc="http://purl.org/dc/elements/1.1/"
   xmlns:cc="http://creativecommons.org/ns#"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:svg="http://www.w3.org/2000/svg"
   xmlns="http://www.w3.org/2000/svg"
   version="1.1"
   id="svg6613"
   viewBox="0 0 62 92"
   height="297mm"
   width="210mm">
  <defs
     id="defs6615" />
  <metadata
     id="metadata6618">
    <rdf:RDF>
      <cc:Work
         rdf:about="">
        <dc:format>image/svg+xml</dc:format>
        <dc:type
           rdf:resource="http://purl.org/dc/dcmitype/StillImage" />
        <dc:title></dc:title>
      </cc:Work>
    </rdf:RDF>
  </metadata>
  <g
     id="layer1">
"""

# y="332.36218"

outer_card = """
    <g
       id="purple-zero">
<!--       transform="matrix(4,0,0,4,2.8571413,-1321.3722)"> -->
      <rect
         style="fill:#ffffff;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:0.5;stroke-miterlimit:4;stroke-dasharray:none"
         id="card-border"
         y="0"
         x="0"
         ry="10"
         rx="10"
         height="90"
         width="60" />
"""
card_color_fill = """
      <rect
         card-fill="rect3757-5-07-1-97"
         style="fill:#%s;fill-opacity:1;fill-rule:evenodd;stroke:none"
         id="card-purple-fill"
         y="5"
         x="5"
         ry="5"
         rx="5"
         height="80"
         width="50" />
      """
card_white_center = """
      <path
         style="fill:#ffffff;fill-opacity:1;fill-rule:evenodd;stroke:none"
         id="card-whitecenter"
         d="m 45,20 c -22.09139,0 -40,17.90861 -40,40 0,5.52285 4.47715,10 10,10 22.09139,0 40,-17.90861 40,-40 0,-5.52285 -4.47715,-10 -10,-10 z" />
"""

card_center_zero = """
      <path
         style="fill:#%s;fill-opacity:1;fill-rule:evenodd;stroke:none"
         id="card-center-zero"
         d="m 30,30 c -5.52285,0 -10,4.47715 -10,10 l 0,10 c 0,5.52285 4.47715,10 10,10 5.52285,0 10,-4.47715 10,-10 l 0,-10 c 0,-5.52285 -4.47715,-10 -10,-10 z m 0,5 c 2.76142,0 5,2.23858 5,5 l 0,10 c 0,2.76142 -2.23858,5 -5,5 -2.76142,0 -5,-2.23858 -5,-5 l 0,-10 c 0,-2.76142 2.23858,-5 5,-5 z" />
"""

card_center_outer = """
      <path
         style="fill:#%s;fill-opacity:1;fill-rule:evenodd;stroke:none"
         id="card-center-zero"
         d="%s" />
"""


card_centers = [
        # zero
        "m 30,30 c -5.52285,0 -10,4.47715 -10,10 l 0,10 c 0,5.52285 4.47715,10 10,10 5.52285,0 10,-4.47715 10,-10 l 0,-10 c 0,-5.52285 -4.47715,-10 -10,-10 z m 0,5 c 2.76142,0 5,2.23858 5,5 l 0,10 c 0,2.76142 -2.23858,5 -5,5 -2.76142,0 -5,-2.23858 -5,-5 l 0,-10 c 0,-2.76142 2.23858,-5 5,-5 z",
        # one
        "m 28,30 -5,5 0,6 5,-5 0,24 5,0 0,-30 z",
        # two
        "m 29,30 c -5.54,0 -10,4.45999 -10,9.99999 l 0,1 5,0 0,-1 c 0,-2.77 2.23,-5 5,-5 2.77,0 5,2.23 5,5 0,1.1275 -0.93551,3.34015 -1.91245,4.10902 -5.30481,4.17494 -5.24881,3.48544 -13.08755,8.89098 l 0,7 10,0 10,0 0,-5 0,-2 -5,0 0,2 -5,0 -4,0 c 6.19007,-4.35874 6.6427,-4.25311 11.49308,-8.59375 1.55408,-1.39076 2.50692,-4.15105 2.50692,-6.40625 0,-5.54 -4.46,-9.99999 -10,-9.99999 z",
        # three
        "m 30,30 c -4.14214,0 -7.5,3.35786 -7.5,7.5 l 5,0 c 0,-1.38071 1.11929,-2.5 2.5,-2.5 1.38071,0 2.5,1.11929 2.5,2.5 0,1.38071 -1.11929,2.5 -2.5,2.5 l -3,0 0,5 3,0 c 2.77,0 5,2.23 5,5 0,2.77 -2.23,5 -5,5 -2.77,0 -5,-2.23 -5,-5 l -5,0 c 0,5.54 4.46,10 10,10 5.54,0 10,-4.46 10,-10 0,-3.29394 -1.58832,-6.18011 -4.03125,-8 0.95194,-1.25738 1.53125,-2.80132 1.53125,-4.5 0,-4.14214 -3.35786,-7.5 -7.5,-7.5 z",
        # four
        "M 28.8,30 19,50 l 0,5 12,0 0,5.00002 5,0 0,-5.00002 3,0 0,-5 -3,0 0,-9.99997 -5,0 0,9.99997 -6.8,0 9.8,-19.99998 z",
        # five
        "m 21,30 0,10 0,5 10,0 c 2.77,0 5,2.23 5,5 0,2.77 -2.23,5 -5,5 -2.77,0 -5,-2.23 -5,-5 l -5,0 c 0,5.54 4.46,10 10,10 5.54,0 10,-4.46 10,-10 0,-5.54 -4.46,-10 -10,-10 l -5,0 0,-5 5,0 9,0 0,-5 -9,0 -5,0 z",
        # six
        "m 30,30 c -5.52285,0 -10,4.47715 -10,10 l 0,10 c 0,5.52285 4.47715,10 10,10 5.52285,0 10,-4.47715 10,-10 0,-5.52285 -4.47715,-10 -10,-10 -1.817,0 -3.53157,0.49674 -5,1.34375 l 0,-1.34375 c 0,-2.76142 2.23858,-5 5,-5 1.95426,0 3.6151,1.14704 4.4375,2.78125 l 4.5,-2.25 c -1.63927,-3.28436 -5.01726,-5.53125 -8.9375,-5.53125 z m 0,15 c 2.76142,0 5,2.23858 5,5 0,2.76142 -2.23858,5 -5,5 -2.76142,0 -5,-2.23858 -5,-5 0,-2.76142 2.23858,-5 5,-5 z m -5,16 0,2 10,0 0,-2 -10,0 z",
        # seven
        "m 21.5,30 0,10 5,0 0,-5 10,0 -10,25 5,0 10,-25 0,-5 -15,0 -5,0 z",
        # eight
        "m 30,30 c -4.14214,0 -7.5,3.3578 -7.5,7.5 0,1.6987 0.57931,3.2426 1.53125,4.5 -2.44293,1.8199 -4.03125,4.706 -4.03125,8 0,5.54 4.46,10 10,10 5.54,0 10,-4.46 10,-10 0,-3.294 -1.58832,-6.1801 -4.03125,-8 0.95194,-1.2574 1.53125,-2.8013 1.53125,-4.5 0,-4.1422 -3.35786,-7.5 -7.5,-7.5 z m 0,5 c 1.38071,0 2.5,1.1193 2.5,2.5 0,1.3807 -1.11929,2.5 -2.5,2.5 -1.38071,0 -2.5,-1.1193 -2.5,-2.5 0,-1.3807 1.11929,-2.5 2.5,-2.5 z m -0.5,10 c 0.16849,-0.017 0.32687,0 0.5,0 2.77,0 5,2.23 5,5 0,2.77 -2.23,5 -5,5 -2.77,0 -5,-2.23 -5,-5 0,-2.5969 1.9726,-4.7449 4.5,-5 z",
        # nine
        "m 30,30 c -5.52285,0 -10,4.47715 -10,10 0,5.52285 4.47715,10 10,10 1.817,0 3.53157,-0.49674 5,-1.34375 l 0,1.34375 c 0,2.76142 -2.23858,5 -5,5 -1.95426,0 -3.6151,-1.14704 -4.4375,-2.78125 l -4.5,2.25 c 1.63927,3.28436 5.01726,5.53125 8.9375,5.53125 5.52285,0 10,-4.47715 10,-10 l 0,-10 c 0,-5.52285 -4.47715,-10 -10,-10 z m 0,5 c 2.76142,0 5,2.23858 5,5 0,2.76142 -2.23858,5 -5,5 -2.76142,0 -5,-2.23858 -5,-5 0,-2.76142 2.23858,-5 5,-5 z m -5,26 0,2 10,0 0,-2 -10,0 z",
        # A
        "m20.072 59.779 5.9418-29.689 7.8597-0.3606 5.248 29.75-5.319 0.1043-0.86918-6.2557h-6.7315l-1.2034 6.4506zm7.1452-11.259h4.7008l-2.2158-14.418z",
        # B
        "m22.377 29.945h6.3178q5.1144 0 7.446 2.1235t2.3316 5.6092q0 2.2036-0.82733 3.8864-0.78973 1.6828-2.2188 2.444 1.8051 1.0016 2.8581 2.6844 1.053 1.6427 1.053 4.888 0 8.4138-12.448 8.4138h-4.5127v-30.049zm6.6563 12.22q2.1812 0 3.2341-0.76125 1.0906-0.76125 1.0906-3.1251 0-2.0834-1.241-2.8447-1.2034-0.80132-3.3093-0.80132h-1.0906v7.5324h1.3162zm-0.11282 13.142q2.7076 0 3.911-1.4023 1.2034-1.4424 1.2034-3.1251 0-2.6043-1.3162-3.4457-1.2786-0.88145-3.6102-0.88145h-1.2034v8.8546h1.0154z",
        # C
        "m29.08 60.463q-4.8512 0-6.8443-4.6877-1.9555-4.6877-1.9555-11.539 0-3.6861 0.90254-7.0917 0.90255-3.4056 2.8957-5.6092 2.0307-2.2437 5.1144-2.2437 2.3692 0 4.1367 1.5626 1.8051 1.5626 2.7452 4.0867 0.97776 2.4841 0.97776 5.2086l-5.3401 0.28046q0-1.803-0.56409-4.0867-0.56409-2.3238-2.2564-2.3238-1.7675 0-2.4444 3.0049-0.67691 3.005-0.67691 7.2119 0 5.2086 0.75212 8.3738 0.75212 3.1251 2.8957 3.1251 1.5042 0 2.1435-1.8831 0.6393-1.9232 0.82733-4.6476l4.7008 0.48079q0 2.8847-0.90254 5.3688-0.90255 2.444-2.7076 3.9264-1.8051 1.4824-4.3999 1.4824z",
        # D
        "m23.251 29.829h5.7913q5.5657 0 8.3109 3.7662t2.7452 11.379q0 4.0466-1.053 7.4122-1.0154 3.3655-3.2717 5.449-2.2564 2.0434-5.7537 2.0434h-6.7691v-30.049zm6.2802 25.362q2.8581 0 3.9486-2.6043 1.1282-2.6443 1.1282-6.4907v-1.3622q0-2.7646-0.33846-4.888-0.30085-2.1636-1.4666-3.7261-1.1282-1.6026-3.4222-1.6026h-0.6393v20.674h0.78972z",
        # E
        "m23.214 60.07v-30.049h14.328l-0.45127 4.6877h-8.3485v7.1718h5.9418l-0.0376 5.0483h-5.9042v8.4539h9.1007l-0.45127 4.6877h-14.177z",
        # F
        "m24.734 60.209v-30.29h14.328l-0.45127 4.7278h-8.3485v7.8529h5.9042v4.9682h-5.9042v12.26l-5.5281 0.48079z"
]

# 7.5 - 332.36218


topleft = [
        # zero
        "m 12.5,7.5 c -2.76143,0 -5,2.23857 -5,5 l 0,5 c 0,2.76143 2.23857,5 5,5 2.76142,0 5,-2.23857 5,-5 l 0,-5 c 0,-2.76143 -2.23858,-5 -5,-5 z m 0,2.5 c 1.38071,0 2.5,1.11929 2.5,2.5 l 0,5 c 0,1.38071 -1.11929,2.5 -2.5,2.5 -1.38071,0 -2.5,-1.11929 -2.5,-2.5 l 0,-5 c 0,-1.38071 1.11929,-2.5 2.5,-2.5 z",
        # one
        "m 10,7.5 -2.5,2.5 0,3 2.5,-2.5 0,12 2.5,0 0,-15 z",
        # two
        "m 12.5,7.5 c -2.77,0 -5,2.23 -5,5 l 0,0.5 2.5,0 0,-0.5 c 0,-1.385 1.115,-2.5 2.5,-2.5 1.385,0 2.5,1.115 2.5,2.5 0,0.56375 -0.46776,1.67007 -0.95623,2.05451 -2.6524,2.08747 -2.6244,1.74272 -6.54377,4.44549 l 0,3.5 5,0 5,0 0,-2.5 0,-1 -2.5,0 0,1 -2.5,0 -2,0 c 3.09503,-2.17937 3.32135,-2.12655 5.74654,-4.29687 0.77704,-0.69538 1.25346,-2.07553 1.25346,-3.20313 0,-2.77 -2.23,-5 -5,-5 z",
        # three
        "m 12.5,7.5 c -2.07107,0 -3.75,1.67893 -3.75,3.75 l 2.5,0 c 0,-0.69036 0.55965,-1.25 1.25,-1.25 0.69035,0 1.25,0.55964 1.25,1.25 0,0.69035 -0.55965,1.25 -1.25,1.25 l -1.5,0 0,2.49999 1.5,0 c 1.385,0 2.5,1.115 2.5,2.50001 0,1.385 -1.115,2.5 -2.5,2.5 -1.385,0 -2.5,-1.115 -2.5,-2.5 l -2.5,0 c 0,2.77 2.23,5 5,5 2.77,0 5,-2.23 5,-5 0,-1.64697 -0.79416,-3.09006 -2.01563,-4 0.47598,-0.6287 0.76563,-1.40066 0.76563,-2.25 0,-2.07107 -1.67893,-3.75 -3.75,-3.75 z",
        # four
        "m 12.3,7.5 -4.9,10 0,2.50001 6,0 0,2.50001 2.5,0 0,-2.50001 1.5,0 0,-2.50001 -1.5,0 0,-4.99999 -2.5,0 0,4.99999 -3.4,0 4.9,-10 z",
        # five
        "m 7.5,7.5 0,5 0,2.5 5,0 c 1.385,0 2.5,1.115 2.5,2.5 0,1.385 -1.115,2.5 -2.5,2.5 -1.385,0 -2.5,-1.115 -2.5,-2.5 l -2.5,0 c 0,2.77 2.23,5 5,5 2.77,0 5,-2.23 5,-5 0,-2.77 -2.23,-5 -5,-5 l -2.5,0 0,-2.5 2.5,0 4.5,0 0,-2.5 -4.5,0 -2.5,0 z",
        # six
        "m 12.5,7.5 c -2.76143,0 -5,2.23859 -5,5.00001 l 0,4.99998 c 0,2.76143 2.23857,5.00001 5,5.00001 2.76142,0 5,-2.23858 5,-5.00001 0,-2.76141 -2.23858,-4.99998 -5,-4.99998 -0.9085,0 -1.76579,0.24837 -2.5,0.67187 l 0,-0.67187 c 0,-1.38071 1.11929,-2.5 2.5,-2.5 0.97712,0 1.80755,0.57351 2.21874,1.39062 l 2.25,-1.125 c -0.81962,-1.64218 -2.50862,-2.76563 -4.46874,-2.76563 z m 0,7.5 c 1.3807,0 2.49999,1.11928 2.49999,2.49999 0,1.38071 -1.11929,2.50001 -2.49999,2.50001 -1.38071,0 -2.5,-1.1193 -2.5,-2.50001 0,-1.38071 1.11929,-2.49999 2.5,-2.49999 z",
        # seven
        "m 7.5,7.5 0,5 2.5,0 0,-2.5 5,0 -5,12.5 2.5,0 5,-12.5 0,-2.5 -7.5,0 -2.5,0 z",
        # eight
        "m 12.5,7.5 c -2.07107,0 -3.75,1.67889 -3.75,3.75 0,0.84935 0.28965,1.6213 0.76562,2.25 -1.22146,0.90994 -2.01562,2.353 -2.01562,4 0,2.77 2.23,5 5,5 2.77,0 5,-2.23 5,-5 0,-1.647 -0.79416,-3.09006 -2.01563,-4 0.47598,-0.6287 0.76563,-1.40065 0.76563,-2.25 0,-2.07111 -1.67893,-3.75 -3.75,-3.75 z m 0,2.5 c 0.69035,0 1.25,0.55965 1.25,1.25 0,0.69034 -0.55965,1.25 -1.25,1.25 -0.69035,0 -1.25,-0.55966 -1.25,-1.25 0,-0.69035 0.55965,-1.25 1.25,-1.25 z m -0.25,4.99999 c 0.0842,-0.009 0.16343,0 0.25,0 1.385,0 2.5,1.115 2.5,2.50001 0,1.385 -1.115,2.5 -2.5,2.5 -1.385,0 -2.5,-1.115 -2.5,-2.5 0,-1.29845 0.9863,-2.37245 2.25,-2.50001 z",
        # nine
        "m 12.5,22.5 c 2.76143,0 5,-2.23859 5,-5.00001 l 0,-4.99998 c 0,-2.76143 -2.23857,-5.00001 -5,-5.00001 -2.76142,0 -5,2.23858 -5,5.00001 0,2.76141 2.23858,4.99998 5,4.99998 0.9085,0 1.76579,-0.24837 2.5,-0.67187 l 0,0.67187 c 0,1.38071 -1.11929,2.5 -2.5,2.5 -0.97712,0 -1.80755,-0.57351 -2.21874,-1.39062 l -2.25,1.125 c 0.81962,1.64218 2.50862,2.76563 4.46874,2.76563 z m 0,-7.5 c -1.3807,0 -2.49999,-1.11928 -2.49999,-2.49999 0,-1.38071 1.11929,-2.50001 2.49999,-2.50001 1.38071,0 2.5,1.1193 2.5,2.50001 0,1.38071 -1.11929,2.49999 -2.5,2.49999 z",
        "","","","","","",

        ]
# y="332.36218"

bottomright = [
        # zero
        "m 47.5,67.5 c -2.76143,0 -5,2.23857 -5,5 l 0,5 c 0,2.76143 2.23857,5 5,5 2.76142,0 5,-2.23857 5,-5 l 0,-5 c 0,-2.76143 -2.23858,-5 -5,-5 z m 0,2.5 c 1.38071,0 2.5,1.11929 2.5,2.5 l 0,5 c 0,1.38071 -1.11929,2.5 -2.5,2.5 -1.38071,0 -2.5,-1.11929 -2.5,-2.5 l 0,-5 c 0,-1.38071 1.11929,-2.5 2.5,-2.5 z",
        # one
        "m 50,82.5 2.5,-2.5 0,-3 -2.5,2.5 0,-12 -2.5,0 0,15 z",
        # two
        "m 47.5,82.5 c 2.77,0 5,-2.23 5,-5 l 0,-0.5 -2.5,0 0,0.5 c 0,1.385 -1.115,2.5 -2.5,2.5 -1.385,0 -2.5,-1.115 -2.5,-2.5 0,-0.56375 0.46776,-1.67007 0.95623,-2.05451 2.6524,-2.08747 2.6244,-1.74272 6.54377,-4.44549 l 0,-3.5 -5,0 -5,0 0,2.5 0,1 2.5,0 0,-1 2.5,0 2,0 c -3.09503,2.17937 -3.32135,2.12655 -5.74654,4.29687 -0.77704,0.69538 -1.25346,2.07553 -1.25346,3.20313 0,2.77 2.23,5 5,5 z",
        # three
        "m 47.5,82.5 c 2.07107,0 3.75,-1.67893 3.75,-3.75 l -2.5,0 c 0,0.69036 -0.55965,1.25 -1.25,1.25 -0.69035,0 -1.25,-0.55964 -1.25,-1.25 0,-0.69035 0.55965,-1.25 1.25,-1.25 l 1.5,0 0,-2.49999 -1.5,0 c -1.385,0 -2.5,-1.115 -2.5,-2.50001 0,-1.385 1.115,-2.5 2.5,-2.5 1.385,0 2.5,1.115 2.5,2.5 l 2.5,0 c 0,-2.77 -2.23,-5 -5,-5 -2.77,0 -5,2.23 -5,5 0,1.64697 0.79416,3.09006 2.01563,4 -0.47598,0.6287 -0.76563,1.40066 -0.76563,2.25 0,2.07107 1.67893,3.75 3.75,3.75 z",
        # four
        "m 47.5,82.5 4.9,-10 0,-2.50001 -6,0 0,-2.50001 -2.5,0 0,2.50001 -1.5,0 0,2.50001 1.5,0 0,4.99999 2.5,0 0,-4.99999 3.4,0 -4.9,10 z",
        # five
        "m 52.5,82.5 0,-5 0,-2.5 -5,0 c -1.385,0 -2.5,-1.115 -2.5,-2.5 0,-1.385 1.115,-2.5 2.5,-2.5 1.385,0 2.5,1.115 2.5,2.5 l 2.5,0 c 0,-2.77 -2.23,-5 -5,-5 -2.77,0 -5,2.23 -5,5 0,2.77 2.23,5 5,5 l 2.5,0 0,2.5 -2.5,0 -4.5,0 0,2.5 4.5,0 2.5,0 z",
        # six
        "m 47.5,82.5 c 2.76143,0 5,-2.23859 5,-5.00001 l 0,-4.99998 c 0,-2.76143 -2.23857,-5.00001 -5,-5.00001 -2.76142,0 -5,2.23858 -5,5.00001 0,2.76141 2.23858,4.99998 5,4.99998 0.9085,0 1.76579,-0.24837 2.5,-0.67187 l 0,0.67187 c 0,1.38071 -1.11929,2.5 -2.5,2.5 -0.97712,0 -1.80755,-0.57351 -2.21874,-1.39062 l -2.25,1.125 c 0.81962,1.64218 2.50862,2.76563 4.46874,2.76563 z m 0,-7.5 c -1.3807,0 -2.49999,-1.11928 -2.49999,-2.49999 0,-1.38071 1.11929,-2.50001 2.49999,-2.50001 1.38071,0 2.5,1.1193 2.5,2.50001 0,1.38071 -1.11929,2.49999 -2.5,2.49999 z",
        # seven
        "m 52.5,82.5 0,-5 -2.5,0 0,2.5 -5,0 5,-12.5 -2.5,0 -5,12.5 0,2.5 7.5,0 2.5,0 z",
        # eight
        "m 47.5,82.5 c -2.07107,0 -3.75,-1.67889 -3.75,-3.75 0,-0.84935 0.28965,-1.6213 0.76562,-2.25 -1.22146,-0.90994 -2.01562,-2.353 -2.01562,-4 0,-2.77 2.23,-5 5,-5 2.77,0 5,2.23 5,5 0,1.647 -0.79416,3.09006 -2.01563,4 0.47598,0.6287 0.76563,1.40065 0.76563,2.25 0,2.07111 -1.67893,3.75 -3.75,3.75 z m 0,-2.5 c 0.69035,0 1.25,-0.55965 1.25,-1.25 0,-0.69034 -0.55965,-1.25 -1.25,-1.25 -0.69035,0 -1.25,0.55966 -1.25,1.25 0,0.69035 0.55965,1.25 1.25,1.25 z m -0.25,-4.99999 c 0.0842,0.009 0.16343,0 0.25,0 1.385,0 2.5,-1.115 2.5,-2.50001 0,-1.385 -1.115,-2.5 -2.5,-2.5 -1.385,0 -2.5,1.115 -2.5,2.5 0,1.29845 0.9863,2.37245 2.25,2.50001 z",
        # nine
        "m 47.5,67.5 c -2.76143,0 -5,2.23859 -5,5.00001 l 0,4.99998 c 0,2.76143 2.23857,5.00001 5,5.00001 2.76142,0 5,-2.23858 5,-5.00001 0,-2.76141 -2.23858,-4.99998 -5,-4.99998 -0.9085,0 -1.76579,0.24837 -2.5,0.67187 l 0,-0.67187 c 0,-1.38071 1.11929,-2.5 2.5,-2.5 0.97712,0 1.80755,0.57351 2.21874,1.39062 l 2.25,-1.125 c -0.81962,-1.64218 -2.50862,-2.76563 -4.46874,-2.76563 z m 0,7.5 c 1.3807,0 2.49999,1.11928 2.49999,2.49999 0,1.38071 -1.11929,2.50001 -2.49999,2.50001 -1.38071,0 -2.5,-1.1193 -2.5,-2.50001 0,-1.38071 1.11929,-2.49999 2.5,-2.49999 z",
        "","","","","","",



        ]


matrix_transform_upper = """
<g id="mat" transform="matrix(0.5,0,0,0.5,-2.2830149,-7.5007809)">
"""
matrix_transform_lower = """
<g id="mat2" transform="matrix(-0.5,0,0,-0.5,61.685933,98.257762)">
"""



matrix_close_group = """</g>"""

card_topleft_outer = """
      <path
         style="fill:#ffffff;fill-opacity:1;fill-rule:evenodd;stroke:none"
         id="card-topleft-zero"
         d="%s" />
         """

card_bottomright_outer = """
      <path
         style="fill:#ffffff;fill-opacity:1;fill-rule:evenodd;stroke:none"
         id="card-bottomright-zero"
         d="%s" />
"""


end_svg = """
    </g>
  </g>
</svg>
"""
