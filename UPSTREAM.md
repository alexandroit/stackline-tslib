# Upstream origin and triage

- Original package: `tslib@2.8.1`
- Repository: https://github.com/Microsoft/tslib
- Source commit: https://github.com/Microsoft/tslib/commit/d72d6f70b36286bc3f94a3dda1e64dcb568b1370
- Source directory: `.`
- npm tarball: https://registry.npmjs.org/tslib/-/tslib-2.8.1.tgz
- SHA512 integrity: `sha512-oJFu94HQb+KVduSUQL7wnpmqnfmLsOA/nAh6b6EH0wCEoK0/mPeXU6c3wKDV83MkOuHPRHtSXKKU99IBazS/2w==`
- npm last-release age selects maintenance scope; it does not imply no ongoing source development.

## Reviewed issues

Primary-source snapshot: `2026-09-29T00:21:42.770647+00:00`. Most recently updated 100 open and 30 closed issue/PR entries; PRs removed. This is triage evidence, not a claim of exhaustive review.

Maintenance adoption with preserved runtime payload. No runtime defect correction is claimed. Reports remain visible for subsequent targeted reproduction.

- [286: __extends继承Array时，不符合预期](https://github.com/microsoft/tslib/issues/286)
- [231: Regression failure upgrading from 2.5.0 to 2.5.1+, webpack fails to transpile new export statement for ES5.](https://github.com/microsoft/tslib/issues/231)
- [161: Wrong exports in tslib](https://github.com/microsoft/tslib/issues/161)
- [268: End of life support for tslib v2.3.0](https://github.com/microsoft/tslib/issues/268)
- [264: import error: '__spreadArray' is not exported from 'tslib' (imported as '__spreadArray').](https://github.com/microsoft/tslib/issues/264)
- [143: modules/index.js should re-export tslib.es6.js instead of tslib.js](https://github.com/microsoft/tslib/issues/143)
- [232: Performance improvement](https://github.com/microsoft/tslib/issues/232)
- [149: export '__spreadArray' (imported as '__spreadArray') was not found in 'tslib'](https://github.com/microsoft/tslib/issues/149)
- [214: calls to tslib __setFunctionName fail on Cobalt 9](https://github.com/microsoft/tslib/issues/214)
- [209: Cannot find module '...node_modules/tslib/modules/index.js' imported from chunks/app/server.mjs](https://github.com/microsoft/tslib/issues/209)
- [212: tslib >=2.5.1 regression - increases bundle size caused by noop `Object.create;` statements](https://github.com/microsoft/tslib/issues/212)
- [210: Generate SLSA Build L3 provenance](https://github.com/microsoft/tslib/issues/210)
- [173: tslib should follow standards for ESM/CJS detection](https://github.com/microsoft/tslib/issues/173)
- [190: __importDefault method may return an object with undefined default property](https://github.com/microsoft/tslib/issues/190)
- [147: 'tslib' does not provide an export named '__decorate'](https://github.com/microsoft/tslib/issues/147)
- [180: Is this project dead from community??](https://github.com/microsoft/tslib/issues/180)
- [170: Package tslib has been ignored because it contains invalid configuration](https://github.com/microsoft/tslib/issues/170)
- [175: TypeError when spreadArray is used on a string containing an emoji/Unicode character](https://github.com/microsoft/tslib/issues/175)
- [74: __spread does not work in IE11](https://github.com/microsoft/tslib/issues/74)
- [156: main.js:1 Uncaught Error: Cannot find module 'tslib'](https://github.com/microsoft/tslib/issues/156)
- [150: question: why isn't it tslib distributed together with tsc?](https://github.com/microsoft/tslib/issues/150)
- [148: Document compatibility of tslib with typescript](https://github.com/microsoft/tslib/issues/148)
- [125: __spread Performance Issues](https://github.com/microsoft/tslib/issues/125)
- [128: Version 1.14.0 removes default export](https://github.com/microsoft/tslib/issues/128)
- [145: 2.1.0 version with node and jest mocking causes errors](https://github.com/microsoft/tslib/issues/145)
- [132: Dead tslib.es6.js code](https://github.com/microsoft/tslib/issues/132)
- [22: Document correspondence between TypeScript and tslib versions](https://github.com/microsoft/tslib/issues/22)
- [115: v1.13.0 Error with older typescript version -- node_modules/tslib/tslib.d.ts(37,78): error TS2304: Cannot find name 'PropertyKey'. (When targeting es3)](https://github.com/microsoft/tslib/issues/115)
- [104: "constructor" is enumerable when targetting es5](https://github.com/microsoft/tslib/issues/104)
- [114: __importStar can result in undefined imports when importing cyclical dependencies](https://github.com/microsoft/tslib/issues/114)
- [32: tslib is polluting window object](https://github.com/microsoft/tslib/issues/32)
- [61: Document helpers needed per target platform](https://github.com/microsoft/tslib/issues/61)
- [48: Lint tslib](https://github.com/microsoft/tslib/issues/48)
- [46: tslib __decorate was conflict with property decorator definition](https://github.com/microsoft/tslib/issues/46)
- [14: Override helpers](https://github.com/microsoft/tslib/issues/14)
- [8: __awaiter helper with arrow functions from TypeScript compiler to tslib](https://github.com/microsoft/tslib/issues/8)

The structured snapshot in `.stackline/issue-triage.json` also records recently closed reports. Issues for unrelated packages in shared monorepositories were qualified as outside this fork’s runtime scope. No maintainer was contacted.
