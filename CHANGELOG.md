# Changelog

## 0.7.0 (2026-07-12)

Full Changelog: [v0.6.0...v0.7.0](https://github.com/ALbot-developers/api-sdk-py/compare/v0.6.0...v0.7.0)

### Features

* **api:** api update ([e529a4a](https://github.com/ALbot-developers/api-sdk-py/commit/e529a4a658751db1ead55d5b3dd87e0ddbddb23d))
* **api:** api update ([ffd1016](https://github.com/ALbot-developers/api-sdk-py/commit/ffd1016b07e208e95a9a4617445151ad13499f24))
* **api:** api update ([97919bd](https://github.com/ALbot-developers/api-sdk-py/commit/97919bd10048a2d9df52823f4d30b10d0054c2c0))

## 0.6.0 (2026-07-05)

Full Changelog: [v0.5.0...v0.6.0](https://github.com/ALbot-developers/api-sdk-py/compare/v0.5.0...v0.6.0)

### Features

* **api:** api update ([b82a4f9](https://github.com/ALbot-developers/api-sdk-py/commit/b82a4f944455edd00239736f599fb3f58a6e1ed9))

## 0.5.0 (2026-05-12)

Full Changelog: [v0.4.1...v0.5.0](https://github.com/ALbot-developers/api-sdk-py/compare/v0.4.1...v0.5.0)

### Features

* **internal/types:** support eagerly validating pydantic iterators ([9b67a8b](https://github.com/ALbot-developers/api-sdk-py/commit/9b67a8b15e16e704404b228edddd0c381d1fbc4d))

## 0.4.1 (2026-05-11)

Full Changelog: [v0.4.0...v0.4.1](https://github.com/ALbot-developers/api-sdk-py/compare/v0.4.0...v0.4.1)

### Bug Fixes

* **client:** add missing f-string prefix in file type error message ([7896577](https://github.com/ALbot-developers/api-sdk-py/commit/789657772dade393bfbc9ece09a7a25b727d5f99))

## 0.4.0 (2026-05-03)

Full Changelog: [v0.3.2...v0.4.0](https://github.com/ALbot-developers/api-sdk-py/compare/v0.3.2...v0.4.0)

### Features

* support setting headers via env ([2b59e68](https://github.com/ALbot-developers/api-sdk-py/commit/2b59e687e8670e6ee34099843992f4b0d0e3db07))


### Bug Fixes

* use correct field name format for multipart file arrays ([2abbf04](https://github.com/ALbot-developers/api-sdk-py/commit/2abbf04ecec75dcee281fc078729eafadd119c32))


### Performance Improvements

* **client:** optimize file structure copying in multipart requests ([241a556](https://github.com/ALbot-developers/api-sdk-py/commit/241a5566f6badb021985785ceee21309771c91dc))


### Chores

* **internal:** more robust bootstrap script ([b5e6e87](https://github.com/ALbot-developers/api-sdk-py/commit/b5e6e877f9ae989bfe3d75796cb4124d5e8498ba))
* **internal:** reformat pyproject.toml ([848b545](https://github.com/ALbot-developers/api-sdk-py/commit/848b5451b3b7f492354c194f28d53361aeab8544))

## 0.3.2 (2026-04-11)

Full Changelog: [v0.3.1...v0.3.2](https://github.com/ALbot-developers/api-sdk-py/compare/v0.3.1...v0.3.2)

### Bug Fixes

* ensure file data are only sent as 1 parameter ([57ce01c](https://github.com/ALbot-developers/api-sdk-py/commit/57ce01c3a9c609bb08df42a893bd71b4b2c0bb4b))

## 0.3.1 (2026-04-10)

Full Changelog: [v0.3.0...v0.3.1](https://github.com/ALbot-developers/api-sdk-py/compare/v0.3.0...v0.3.1)

### Bug Fixes

* **client:** preserve hardcoded query params when merging with user params ([0f8a613](https://github.com/ALbot-developers/api-sdk-py/commit/0f8a613a4418aa6fc171883675ecdb8dcd262ade))

## 0.3.0 (2026-03-28)

Full Changelog: [v0.2.0...v0.3.0](https://github.com/ALbot-developers/api-sdk-py/compare/v0.2.0...v0.3.0)

### Features

* **api:** api update ([2aa61a1](https://github.com/ALbot-developers/api-sdk-py/commit/2aa61a148228c7aa687f7bfe73c88605e0472a4f))
* **internal:** implement indices array format for query and form serialization ([91948a4](https://github.com/ALbot-developers/api-sdk-py/commit/91948a4d99d45a3a56b780c58e1b1ad7c4c9525d))


### Chores

* **ci:** skip lint on metadata-only changes ([c7786f7](https://github.com/ALbot-developers/api-sdk-py/commit/c7786f7ddb3cb4527bafe20e34252923ff999404))
* **internal:** update gitignore ([840c12a](https://github.com/ALbot-developers/api-sdk-py/commit/840c12a0d9a389b7ad973cfb6797e82aea6e5f8d))

## 0.2.0 (2026-03-20)

Full Changelog: [v0.1.1...v0.2.0](https://github.com/ALbot-developers/api-sdk-py/compare/v0.1.1...v0.2.0)

### Features

* **api:** api update ([ab3a673](https://github.com/ALbot-developers/api-sdk-py/commit/ab3a6735434238670cb1c7eb40767f7ee4d2b1a8))


### Bug Fixes

* sanitize endpoint path params ([32bbbd6](https://github.com/ALbot-developers/api-sdk-py/commit/32bbbd6c64cc9a0603cf8215378ad6e824c22ce8))

## 0.1.1 (2026-03-18)

Full Changelog: [v0.1.0...v0.1.1](https://github.com/ALbot-developers/api-sdk-py/compare/v0.1.0...v0.1.1)

### Bug Fixes

* **deps:** bump minimum typing-extensions version ([9fe303d](https://github.com/ALbot-developers/api-sdk-py/commit/9fe303df5bd2a499b741017d7dccf94a36e9ce94))
* **pydantic:** do not pass `by_alias` unless set ([2309226](https://github.com/ALbot-developers/api-sdk-py/commit/230922689585d0f0134acff0804b2183c4b6cf44))


### Chores

* **internal:** tweak CI branches ([eb955bc](https://github.com/ALbot-developers/api-sdk-py/commit/eb955bc9fd1be60230b7cf4a100b3b552ed015b1))

## 0.1.0 (2026-03-11)

Full Changelog: [v0.0.1...v0.1.0](https://github.com/ALbot-developers/api-sdk-py/compare/v0.0.1...v0.1.0)

### Features

* **api:** api update ([00dc5bd](https://github.com/ALbot-developers/api-sdk-py/commit/00dc5bd2231e8175777fefe542563fcd7bee3e9b))
* **api:** manual updates ([a93913a](https://github.com/ALbot-developers/api-sdk-py/commit/a93913acf82dbdc8c2a1cd58c5092963188e0cb3))
* **api:** manual updates ([1be4f6a](https://github.com/ALbot-developers/api-sdk-py/commit/1be4f6a24a73cd586c15121a0f88c629dd9ed5c1))
* improve future compat with pydantic v3 ([6187f86](https://github.com/ALbot-developers/api-sdk-py/commit/6187f86e7f4110d3a04ce62b32ab8cc9d51d7106))
* **types:** replace List[str] with SequenceNotStr in params ([6307a2c](https://github.com/ALbot-developers/api-sdk-py/commit/6307a2cecc9557d9f5e6533438762540d93a5ae8))


### Bug Fixes

* avoid newer type syntax ([d6c6c37](https://github.com/ALbot-developers/api-sdk-py/commit/d6c6c371543aa4023e50abdaed540f5750e0034f))


### Chores

* do not install brew dependencies in ./scripts/bootstrap by default ([ef77409](https://github.com/ALbot-developers/api-sdk-py/commit/ef77409c5a8586a4b22f7ce24fbaa33569f2c4cb))
* **internal:** add Sequence related utils ([f6af8eb](https://github.com/ALbot-developers/api-sdk-py/commit/f6af8eb6e18e66869f76e22fbbc2271435d13fb3))
* **internal:** change ci workflow machines ([ab05c65](https://github.com/ALbot-developers/api-sdk-py/commit/ab05c659b78a13c8035e809ffdb390be319f898b))
* **internal:** codegen related update ([3c76127](https://github.com/ALbot-developers/api-sdk-py/commit/3c7612779860522d8212f4dd5e04fb17e7b07776))
* **internal:** codegen related update ([ceb4cff](https://github.com/ALbot-developers/api-sdk-py/commit/ceb4cffae27fc8934cb73c91eb3e210e5eea18d8))
* **internal:** codegen related update ([9d1c4dc](https://github.com/ALbot-developers/api-sdk-py/commit/9d1c4dc439c2cda8f0ff5bb4fd0cba75a7247a63))
* **internal:** codegen related update ([3e100c2](https://github.com/ALbot-developers/api-sdk-py/commit/3e100c24ba55012a728355ec0c67adf9a245397b))
* **internal:** codegen related update ([b1f6edf](https://github.com/ALbot-developers/api-sdk-py/commit/b1f6edf0ae8ca4436fa1c9067e85dde3d2e86645))
* **internal:** codegen related update ([d50d9a1](https://github.com/ALbot-developers/api-sdk-py/commit/d50d9a1b81b3f7afb29f80801d98aefcdb1e9f18))
* **internal:** codegen related update ([0c49400](https://github.com/ALbot-developers/api-sdk-py/commit/0c494007104c32c6bf1fd4e09691d5c2e69cc90a))
* **internal:** codegen related update ([b4181e7](https://github.com/ALbot-developers/api-sdk-py/commit/b4181e743b9c920f43c5a40ab7fa5a468a52f0f5))
* **internal:** codegen related update ([c0fa3a6](https://github.com/ALbot-developers/api-sdk-py/commit/c0fa3a638aea6e05e5d4504e4bbf5e14312ae4d9))
* **internal:** codegen related update ([ecbee08](https://github.com/ALbot-developers/api-sdk-py/commit/ecbee08d64feefe4676b797a6d4e95d9ea70f11f))
* **internal:** codegen related update ([3869aad](https://github.com/ALbot-developers/api-sdk-py/commit/3869aad036e890a306f27c5642b8587d27b8e09f))
* **internal:** codegen related update ([72e40fe](https://github.com/ALbot-developers/api-sdk-py/commit/72e40fe4749b0eadd337c4b8de27015857894a09))
* **internal:** update pydantic dependency ([db880f6](https://github.com/ALbot-developers/api-sdk-py/commit/db880f61334cae131ed562feb80bcc81c76f22cc))
* **internal:** update pyright exclude list ([77af0e0](https://github.com/ALbot-developers/api-sdk-py/commit/77af0e0d8fa5a9df84cd4a8a1a135239b5e8cb49))
* **tests:** simplify `get_platform` test ([002fc0a](https://github.com/ALbot-developers/api-sdk-py/commit/002fc0af7b6433f57287614950481581bf781265))
* **types:** change optional parameter type from NotGiven to Omit ([f12105c](https://github.com/ALbot-developers/api-sdk-py/commit/f12105c6e6d35447541b9bbc694540f620bbb888))
* update github action ([f158da9](https://github.com/ALbot-developers/api-sdk-py/commit/f158da9ecbd5e1d462f49a259ac144f45c312baf))
* update SDK settings ([827809d](https://github.com/ALbot-developers/api-sdk-py/commit/827809d9d8094fd60b2db6972782e9329223179d))
