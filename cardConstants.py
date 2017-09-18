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


newLetters = [
        # A
        "m 26.562349,30.123441 -8.55041,29.820169 5.496692,0 1.221487,-4.552698 8.945596,0 1.11371,4.552698 5.855953,0 -8.227075,-29.820169 -5.855953,0 z m 2.838161,7.739585 3.017792,13.051067 -6.502623,0 3.484831,-13.051067 z" ,
        # B
        "m 19.292843,30.054537 0,29.820169 11.208941,0 c 7.005588,0 9.735971,-2.162532 9.735971,-8.081038 0,-4.249185 -1.47297,-6.525534 -3.556683,-7.663708 1.580747,-1.176114 2.622604,-3.262767 2.622604,-6.715229 0,-5.349419 -2.4789,-7.360194 -9.304857,-7.360194 l -10.705976,0 z m 5.999657,16.46559 4.41891,0 c 3.269274,0 4.59854,0.531148 4.59854,4.249183 0,3.56628 -1.077784,4.325063 -4.59854,4.325063 l -4.41891,0 0,-8.574246 z m 0,-11.723197 4.382983,0 c 3.197423,0 4.203353,0.720844 4.203353,3.869793 0,3.300706 -1.041856,3.831854 -4.059648,3.831854 l -4.526688,0 0,-7.701647 z" ,
        # C
        "m 39.303676,32.065312 c -1.616674,-1.441689 -4.59854,-2.579863 -9.700045,-2.579863 -8.119296,0 -10.777827,2.883376 -10.777827,15.441233 0,12.406101 2.622604,15.517111 10.382641,15.517111 6.43077,0 10.023379,-2.162531 10.023379,-8.612186 l 0,-0.758783 -5.281135,0 0,0.720844 c 0,2.503984 -1.365192,3.604218 -4.41891,3.604218 -3.628535,0 -4.706318,-1.403747 -4.706318,-10.471204 0,-9.067456 1.11371,-10.395326 4.850022,-10.395326 1.868158,0 3.305201,0.303513 4.095575,0.720843 l 0,3.035133 5.532618,0 0,-6.22202 z" ,
        # D
        "m 19.292843,30.054537 0,29.820169 9.735971,0 c 8.442632,0 10.634123,-4.704455 10.634123,-14.872146 0,-10.167691 -2.191491,-14.948023 -10.634123,-14.948023 l -9.735971,0 z m 5.820027,5.045906 3.915944,0 c 3.772239,0 4.706318,2.769558 4.706318,9.902117 0,7.13256 -0.934079,9.82624 -4.706318,9.82624 l -3.915944,0 0,-19.728357 z" ,
        # E
        "m 19.292843,30.054537 0,29.820169 20.585651,0 0,-5.045906 -14.585994,0 0,-8.118978 13.97525,0 0,-4.818272 -13.97525,0 0,-6.791107 14.514142,0 0,-5.045906 -20.513799,0 z" ,
        # F
        "m 19.292843,30.054537 0,29.820169 5.999657,0 0,-12.709615 14.226733,0 0,-4.932089 -14.226733,0 0,-7.132559 14.550068,0 0,-5.045906 -20.549725,0 z" ,
]

newLetters2 = [
     # letter-A"
     "m 26.688065,30.093401 -8.225352,29.832883 4.602788,0 1.449026,-5.796103 8.651536,0 1.576881,5.796103 4.474933,0 -8.651536,-29.832883 -3.878276,0 z m 1.960447,7.458221 0.127856,0 3.366854,12.82814 -6.69109,0 3.19638,-12.82814 z",
     # letter-B"
     "m 20.124831,30.093401 0,29.832883 9.802233,0 c 5.753485,0 7.586077,-2.94067 7.586077,-7.628694 0,-3.281617 -0.894987,-5.455156 -3.025907,-6.520616 1.832591,-1.193315 2.642341,-3.494709 2.642341,-7.117274 0,-5.838721 -2.088302,-8.566299 -7.75655,-8.566299 l -9.248194,0 z m 4.474932,4.091367 4.730644,0 c 2.684959,0 3.622564,1.278552 3.622564,5.07159 0,3.75042 -0.894986,5.028972 -3.622564,5.028972 l -4.730644,0 0,-10.100562 z m 0,13.637889 5.284683,0 c 2.429249,0 3.19638,0.980224 3.19638,3.920894 0,2.94067 -0.767131,4.091367 -3.19638,4.091367 l -5.284683,0 0,-8.012261 z",
     # letter-C"
     "m 38.87693,35.932122 c -0.80975,-3.963511 -3.579946,-6.392761 -8.694155,-6.392761 -7.372985,0 -10.825075,5.028972 -10.825075,15.598337 0,10.185799 3.19638,15.342626 10.69722,15.342626 5.369919,0 7.927023,-2.642341 8.907246,-6.392761 l -3.537327,-1.363789 c -0.554039,1.917828 -2.003065,3.622564 -5.114209,3.622564 -4.133986,0 -6.392761,-3.025906 -6.392761,-11.251259 0,-8.438444 2.344012,-11.421732 6.43538,-11.421732 2.94067,0 4.517551,1.534262 4.986353,3.665183 l 3.537328,-1.406408 z",
     # letter-D"
     "m 20.124831,30.093401 0,29.832883 8.225352,0 c 7.032037,0 10.782457,-4.347077 10.782457,-14.916441 0,-10.356273 -3.579946,-14.916442 -10.526746,-14.916442 l -8.481063,0 z m 4.517551,4.091367 3.835657,0 c 4.091367,0 6.094432,3.068525 6.094432,10.867693 0,7.75655 -2.003065,10.782457 -6.094432,10.782457 l -3.835657,0 0,-21.65015 z",
     # letter-E"
     "m 20.124831,30.093401 0,29.832883 15.470481,0 0,-4.091366 -11.038167,0 0,-7.841787 10.69722,0 0,-3.793038 -10.69722,0 0,-10.015325 10.825075,0 0,-4.091367 -15.257389,0 z",
     # letter-F"
     "m 20.124831,30.093401 0,29.832883 4.517551,0 0,-11.379114 10.398891,0 0,-4.048748 -10.398891,0 0,-10.313654 10.526746,0 0,-4.091367 -15.044297,0 z",
]

newLetters1 = [
        # A
     "m 25.855721,29.928035 -9.102854,30.062368 5.851835,0 1.300407,-4.589675 9.523575,0 1.185666,4.589675 6.234308,0 -8.758629,-30.062368 -6.234308,0 z m 3.021536,7.802446 3.212772,13.157068 -6.922759,0 3.709987,-13.157068 z",
      # "m 25.423097,30.224075 6.461081,0 7.692666,29.788409 -4.301072,0 -2.349484,-9.103233 -8.317931,0 -2.235799,9.103233 -4.414756,0 7.465295,-29.788409 z m 6.612661,16.8684 -3.467384,-14.609043 -3.126329,14.609043 6.593713,0 z",
     #"m 26.562349,30.123441 -8.55041,29.820169 5.496692,0 1.221487,-4.552698 8.945596,0 1.11371,4.552698 5.855953,0 -8.227075,-29.820169 -5.855953,0 z m 2.838161,7.739585 3.017792,13.051067 -6.502623,0 3.484831,-13.051067 z",
     # letter-B"
     "m 19.292843,30.054537 0,29.820169 11.208941,0 c 7.005588,0 9.735971,-2.162532 9.735971,-8.081038 0,-4.249185 -1.47297,-6.525534 -3.556683,-7.663708 1.580747,-1.176114 2.622604,-3.262767 2.622604,-6.715229 0,-5.349419 -2.4789,-7.360194 -9.304857,-7.360194 l -10.705976,0 z m 5.999657,16.46559 4.41891,0 c 3.269274,0 4.59854,0.531148 4.59854,4.249183 0,3.56628 -1.077784,4.325063 -4.59854,4.325063 l -4.41891,0 0,-8.574246 z m 0,-11.723197 4.382983,0 c 3.197423,0 4.203353,0.720844 4.203353,3.869793 0,3.300706 -1.041856,3.831854 -4.059648,3.831854 l -4.526688,0 0,-7.701647 z",
     # letter-C"
     "m 39.303676,32.065312 c -1.616674,-1.441689 -4.59854,-2.579863 -9.700045,-2.579863 -8.119296,0 -10.777827,2.883376 -10.777827,15.441233 0,12.406101 2.622604,15.517111 10.382641,15.517111 6.43077,0 10.023379,-2.162531 10.023379,-8.612186 l 0,-0.758783 -5.281135,0 0,0.720844 c 0,2.503984 -1.365192,3.604218 -4.41891,3.604218 -3.628535,0 -4.706318,-1.403747 -4.706318,-10.471204 0,-9.067456 1.11371,-10.395326 4.850022,-10.395326 1.868158,0 3.305201,0.303513 4.095575,0.720843 l 0,3.035133 5.532618,0 0,-6.22202 z",
     # letter-D"
     "m 19.292843,30.054537 0,29.820169 9.735971,0 c 8.442632,0 10.634123,-4.704455 10.634123,-14.872146 0,-10.167691 -2.191491,-14.948023 -10.634123,-14.948023 l -9.735971,0 z m 5.820027,5.045906 3.915944,0 c 3.772239,0 4.706318,2.769558 4.706318,9.902117 0,7.13256 -0.934079,9.82624 -4.706318,9.82624 l -3.915944,0 0,-19.728357 z",
     # letter-E"
     "m 19.292843,30.054537 0,29.820169 20.585651,0 0,-5.045906 -14.585994,0 0,-8.118978 13.97525,0 0,-4.818272 -13.97525,0 0,-6.791107 14.514142,0 0,-5.045906 -20.513799,0 z",
     # letter-F"
     "m 19.292843,30.054537 0,29.820169 5.999657,0 0,-12.709615 14.226733,0 0,-4.932089 -14.226733,0 0,-7.132559 14.550068,0 0,-5.045906 -20.549725,0 z",
]


matrix_transform_upper = """
<g id="mat" transform="matrix(0.5,0,0,0.5,-2.5,-7.5)">
"""
matrix_transform_lower = """
<g id="mat2" transform="matrix(-0.5,0,0,-0.5,62.5,96.8)">
"""

"""
<g id="mat" transform="matrix(0.5,0,0,0.5,-2.2830149,-7.5007809)">
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


newLetters3 = [
        # A
     #"m 25.395315,30.224075 6.914179,0 8.232131,29.788409 -4.602694,0 -2.514247,-9.103233 -8.901245,0 -2.39259,9.103233 -4.724351,0 7.988817,-29.788409 z m 7.076388,16.8684 -3.710542,-14.609043 -3.34557,14.609043 7.056112,0 z",
     "m 26.373334,29.928035 -8.035469,30.062368 5.165659,0 1.147923,-4.589675 8.406858,0 1.046636,4.589675 5.503284,0 -7.731607,-30.062368 -5.503284,0 z m 2.667235,7.802446 2.836049,13.157068 -6.111008,0 3.274959,-13.157068 z",

     # B
     "m 21.375338,30.224075 9.616025,0 q 1.519332,0 2.846343,0.482581 1.327012,0.460646 2.288614,1.425808 0.961603,0.943226 1.519332,2.369034 0.55773,1.403872 0.55773,3.268389 0,0.987097 -0.307714,1.952259 -0.288479,0.965163 -0.826978,1.820647 -0.519265,0.833549 -1.230851,1.491614 -0.711585,0.63613 -1.538564,0.965162 0.865443,0.175484 1.730885,0.745807 0.865442,0.570323 1.557796,1.51355 0.692354,0.943226 1.115459,2.215484 0.442336,1.250324 0.442336,2.763874 0,2.083872 -0.557728,3.707099 -0.538497,1.623227 -1.634725,2.763873 -1.096226,1.118711 -2.711719,1.710969 -1.615492,0.592259 -3.750249,0.592259 l -9.115992,0 0,-29.788409 z m 8.654422,26.059373 q 1.057764,0 1.903974,-0.263226 0.865441,-0.263225 1.480867,-0.855484 0.615426,-0.592258 0.942371,-1.535485 0.346177,-0.943226 0.346177,-2.303228 0,-1.381936 -0.346177,-2.303227 Q 34.030027,48.079572 33.433833,47.509249 32.856872,46.91699 32.049125,46.6757 31.260612,46.434409 30.337474,46.434409 l -4.596461,0 0,9.849039 4.288747,0 z m 1.134691,-13.161299 q 1.346244,-0.460646 1.961669,-1.75484 0.634658,-1.31613 0.634658,-3.509679 0,-1.864518 -0.961603,-2.895487 -0.961602,-1.052904 -2.654022,-1.052904 l -4.40414,0 0,9.21291 5.423438,0 z",
     #"m 20.850803,30.224075 9.616025,0 q 1.519332,0 2.846343,0.482581 1.327012,0.460646 2.288614,1.425808 0.961603,0.943226 1.519332,2.369034 0.55773,1.403872 0.55773,3.268389 0,0.987097 -0.307714,1.952259 -0.288479,0.965163 -0.826978,1.820647 -0.519265,0.833549 -1.230851,1.491614 -0.711585,0.63613 -1.538564,0.965162 0.865443,0.175484 1.730885,0.745807 0.865442,0.570323 1.557796,1.51355 0.692354,0.943226 1.115459,2.215484 0.442336,1.250324 0.442336,2.763874 0,2.083872 -0.557728,3.707099 -0.538497,1.623227 -1.634725,2.763873 -1.096226,1.118711 -2.711719,1.710969 -1.615492,0.592259 -3.750249,0.592259 l -9.115992,0 0,-29.788409 z m 8.654422,26.059373 q 1.057764,0 1.903974,-0.263226 0.865441,-0.263225 1.480867,-0.855484 0.615426,-0.592258 0.942371,-1.535485 0.346177,-0.943226 0.346177,-2.303228 0,-1.381936 -0.346177,-2.303227 Q 33.505492,48.079572 32.909298,47.509249 32.332337,46.91699 31.52459,46.6757 30.736077,46.434409 29.812939,46.434409 l -4.596461,0 0,9.849039 4.288747,0 z m 1.134691,-13.161299 q 1.346244,-0.460646 1.961669,-1.75484 0.634658,-1.31613 0.634658,-3.509679 0,-1.864518 -0.961603,-2.895487 -0.961602,-1.052904 -2.654022,-1.052904 l -4.40414,0 0,9.21291 5.423438,0 z",
#     "m 20.850803,30.224075 9.616025,0 q 1.519332,0 2.846343,0.482581 1.327012,0.460646 2.288614,1.425808 0.961603,0.943226 1.519332,2.369034 0.55773,1.403872 0.55773,3.268389 0,0.987097 -0.307714,1.952259 -0.288479,0.965163 -0.826978,1.820647 -0.519265,0.833549 -1.230851,1.491614 -0.711585,0.63613 -1.538564,0.965162 0.865443,0.175484 1.730885,0.745807 0.865442,0.570323 1.557796,1.51355 0.692354,0.943226 1.115459,2.215484 0.442336,1.250324 0.442336,2.763874 0,2.083872 -0.557728,3.707099 -0.538497,1.623227 -1.634725,2.763873 -1.096226,1.118711 -2.711719,1.710969 -1.615492,0.592259 -3.750249,0.592259 l -9.115992,0 0,-29.788409 z m 8.654422,26.059373 q 1.057764,0 1.903974,-0.263226 0.865441,-0.263225 1.480867,-0.855484 0.615426,-0.592258 0.942371,-1.535485 0.346177,-0.943226 0.346177,-2.303228 0,-1.381936 -0.346177,-2.303227 Q 33.505492,48.079572 32.909298,47.509249 32.332337,46.91699 31.52459,46.6757 30.736077,46.434409 29.812939,46.434409 l -4.596461,0 0,9.849039 4.288747,0 z m 1.134691,-13.161299 q 1.346244,-0.460646 1.961669,-1.75484 0.634658,-1.31613 0.634658,-3.509679 0,-1.864518 -0.961603,-2.895487 -0.961602,-1.052904 -2.654022,-1.052904 l -4.40414,0 0,9.21291 5.423438,0 z",

     # c
     "m 19.170526,45.381505 q 0,-3.750969 0.811047,-6.668391 0.811048,-2.939357 2.39259,-4.935488 1.581542,-2.018066 3.893028,-3.07097 2.311485,-1.052904 5.31236,-1.052904 1.196295,0 2.352037,0.19742 1.155743,0.175485 2.108724,0.416775 1.094914,0.263226 2.108723,0.592259 -0.06083,0.570322 -0.182486,1.206452 -0.101381,0.570323 -0.324419,1.294194 -0.202761,0.701936 -0.547457,1.469678 -0.750218,-0.329032 -1.642371,-0.570323 -0.770495,-0.219354 -1.764028,-0.394839 -0.993533,-0.175483 -2.108723,-0.175483 -1.80458,0 -3.264466,0.789677 -1.439609,0.789679 -2.473694,2.303228 -1.01381,1.491614 -1.561267,3.663229 -0.547457,2.171614 -0.547457,4.935486 0,2.741937 0.547457,4.82581 0.547457,2.083873 1.561267,3.487744 1.034085,1.403872 2.473694,2.127744 1.459886,0.701936 3.264466,0.701936 1.135466,0 2.169552,-0.175484 1.034085,-0.175484 1.824856,-0.39484 0.932705,-0.24129 1.723476,-0.592258 0.223038,0.504517 0.385248,1.118711 0.141933,0.526451 0.243314,1.272259 0.121657,0.723872 0.08111,1.645163 -0.952981,0.350967 -2.027619,0.592258 -0.912428,0.241291 -2.068171,0.416774 -1.135466,0.175485 -2.331761,0.175485 -6.16396,0 -9.286493,-3.816778 -3.122532,-3.838712 -3.122532,-11.384524 z",

     # d
     "m 21.532256,30.246011 q 0.869289,-0.04387 1.92607,-0.109677 0.920422,-0.04387 2.147651,-0.08775 1.244275,-0.04387 2.727179,-0.04387 2.658998,0 4.70438,0.921291 2.045384,0.899356 3.443062,2.741937 1.414724,1.842583 2.130609,4.628391 0.732928,2.785809 0.732928,6.536779 0,3.75097 -0.784064,6.602585 -0.784063,2.829679 -2.249921,4.738067 -1.448814,1.908389 -3.528286,2.873552 -2.079473,0.965161 -4.687338,0.965161 l -6.56227,0 0,-29.766473 z m 7.141796,25.92776 q 1.585173,0 2.829448,-0.855485 1.244276,-0.877419 2.113562,-2.390969 0.869287,-1.535485 1.3295,-3.575486 0.460211,-2.061938 0.460211,-4.430971 0,-2.741938 -0.460211,-4.803874 -0.460213,-2.083873 -1.3295,-3.487745 -0.869286,-1.403872 -2.113562,-2.105807 -1.244275,-0.701936 -2.829448,-0.701936 -0.869288,0 -1.499949,0.02194 -0.630658,0.02194 -1.02269,0.04387 -0.460211,0.04387 -0.767019,0.06581 l 0,22.22066 3.289658,0 z",


     # e
     "m 21.826706,30.224075 15.795148,0 q 0,0.15355 0.02028,0.329033 0.02028,0.153548 0.02028,0.350968 0.02028,0.175485 0.02028,0.394839 0,0.372904 -0.141934,1.140646 -0.121657,0.745807 -0.567733,1.732905 -1.682923,-0.06581 -3.487504,-0.131613 -1.54099,-0.04387 -3.406399,-0.08775 -1.865409,-0.06581 -3.649713,-0.06581 l 0,8.993555 q 0.588009,0 1.317952,0 0.750219,-0.02194 1.54099,-0.04387 0.811047,-0.02194 1.622095,-0.04387 0.811047,-0.02194 1.581542,-0.04387 1.784305,-0.06581 3.66999,-0.109678 0,0.175485 0.02028,0.372903 0.02028,0.175485 0.02028,0.416775 0.02028,0.219356 0.02028,0.460646 0,0.109678 -0.04055,0.438709 -0.02028,0.307098 -0.101381,0.701936 -0.06083,0.39484 -0.162209,0.789679 -0.08111,0.394838 -0.202762,0.658064 -1.885685,0 -3.629437,-0.02194 -0.750219,0 -1.54099,0 -0.790772,0 -1.540991,0 -0.729942,-0.02194 -1.399056,-0.02194 -0.669114,0 -1.176019,0 l 0,9.827103 q 1.784304,0 3.751094,-0.06581 1.987066,-0.06581 3.690266,-0.131613 1.987066,-0.08774 3.913304,-0.197418 0,0.197418 0.02028,0.416773 0.02028,0.175485 0.02028,0.438711 0.02028,0.24129 0.02028,0.482581 0,0.460645 -0.06083,1.206452 -0.06083,0.745807 -0.263591,1.601292 l -15.693767,0 0,-29.788408 z",

     #i"f"

     "m 22.110573,30.224075 15.795148,0 q 0,0.15355 0.02028,0.329033 0.02028,0.153548 0.02028,0.350968 0.02028,0.175485 0.02028,0.394839 0,0.372904 -0.141933,1.140646 -0.121657,0.745807 -0.567733,1.732905 -1.662647,-0.06581 -3.446952,-0.131613 -1.520714,-0.04387 -3.406399,-0.08775 -1.865409,-0.06581 -3.690265,-0.06581 l 0,9.717426 q 0.547457,0 1.277399,0 0.729943,-0.02194 1.54099,-0.04387 0.811048,-0.02194 1.662647,-0.04387 0.871876,-0.04387 1.682924,-0.06581 1.905961,-0.06581 3.974132,-0.131613 0,0.175484 0.02028,0.372904 0.02028,0.175483 0.02028,0.416774 0.02028,0.219355 0.02028,0.460645 0,0.19742 -0.101381,0.833549 -0.08111,0.63613 -0.405524,1.820647 -2.149276,0 -4.055237,-0.02194 -0.811047,0 -1.662647,0 -0.831324,0 -1.581543,0 -0.750218,-0.02194 -1.37878,-0.02194 -0.628562,0 -1.013809,0 l 0,12.832268 -4.602694,0 0,-29.788408 z",
]
