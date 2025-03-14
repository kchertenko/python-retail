# Changelog

## [1.10.0](https://github.com/googleapis/python-retail/compare/v1.9.0...v1.10.0) (2022-09-02)


### Features

* Release Model Services to v2beta version ([#333](https://github.com/googleapis/python-retail/issues/333)) ([ec20834](https://github.com/googleapis/python-retail/commit/ec208343314664cd5e61f67cd8b464d96aac901a))

## [1.9.0](https://github.com/googleapis/python-retail/compare/v1.8.1...v1.9.0) (2022-08-23)


### Features

* add local inventories info to the Product resource ([33d7202](https://github.com/googleapis/python-retail/commit/33d7202221535337b8176477d8dd2758a880be40))
* release AttributesConfig APIs to v2 version ([33d7202](https://github.com/googleapis/python-retail/commit/33d7202221535337b8176477d8dd2758a880be40))
* release CompletionConfig APIs to v2 version ([33d7202](https://github.com/googleapis/python-retail/commit/33d7202221535337b8176477d8dd2758a880be40))
* release Control and ServingConfig serivces to v2 version ([#319](https://github.com/googleapis/python-retail/issues/319)) ([33d7202](https://github.com/googleapis/python-retail/commit/33d7202221535337b8176477d8dd2758a880be40))


### Documentation

* Improved documentation for Fullfillment and Inventory API in ProductService ([33d7202](https://github.com/googleapis/python-retail/commit/33d7202221535337b8176477d8dd2758a880be40))
* minor documentation format and typo fixes ([33d7202](https://github.com/googleapis/python-retail/commit/33d7202221535337b8176477d8dd2758a880be40))

## [1.8.1](https://github.com/googleapis/python-retail/compare/v1.8.0...v1.8.1) (2022-08-12)


### Bug Fixes

* **deps:** allow protobuf < 5.0.0 ([#313](https://github.com/googleapis/python-retail/issues/313)) ([9c8c730](https://github.com/googleapis/python-retail/commit/9c8c730f97f155b41f795ef73f4a362c97479455))
* **deps:** require proto-plus >= 1.22.0 ([9c8c730](https://github.com/googleapis/python-retail/commit/9c8c730f97f155b41f795ef73f4a362c97479455))

## [1.8.0](https://github.com/googleapis/python-retail/compare/v1.7.0...v1.8.0) (2022-08-09)


### Features

* allow adding labels in search requests ([d981c65](https://github.com/googleapis/python-retail/commit/d981c65fcf7f8f04fd36f728b639dd15756af04d))
* allow disabling spell check in search requests ([d981c65](https://github.com/googleapis/python-retail/commit/d981c65fcf7f8f04fd36f728b639dd15756af04d))
* allow enabling recommendation filtering on custom attributes ([d981c65](https://github.com/googleapis/python-retail/commit/d981c65fcf7f8f04fd36f728b639dd15756af04d))
* allow returning min/max values on search numeric facets ([d981c65](https://github.com/googleapis/python-retail/commit/d981c65fcf7f8f04fd36f728b639dd15756af04d))
* allow skipping default branch protection when doing product full import ([fabe71c](https://github.com/googleapis/python-retail/commit/fabe71c5aacc44cacd4dc6d95fc02878691a8185))
* allow using serving configs as an alias of placements ([d981c65](https://github.com/googleapis/python-retail/commit/d981c65fcf7f8f04fd36f728b639dd15756af04d))
* new model service to manage recommendation models ([fabe71c](https://github.com/googleapis/python-retail/commit/fabe71c5aacc44cacd4dc6d95fc02878691a8185))
* return output BigQuery table on product / event export response ([d981c65](https://github.com/googleapis/python-retail/commit/d981c65fcf7f8f04fd36f728b639dd15756af04d))
* support case insensitive match on search facets ([#301](https://github.com/googleapis/python-retail/issues/301)) ([d981c65](https://github.com/googleapis/python-retail/commit/d981c65fcf7f8f04fd36f728b639dd15756af04d))


### Documentation

* keep the API doc up-to-date with recent changes ([d981c65](https://github.com/googleapis/python-retail/commit/d981c65fcf7f8f04fd36f728b639dd15756af04d))

## [1.7.0](https://github.com/googleapis/python-retail/compare/v1.6.1...v1.7.0) (2022-07-17)


### Features

* add audience parameter ([34642ee](https://github.com/googleapis/python-retail/commit/34642ee4b9709b56773502d1f6d1c473619c0da1))
* allow users to add labels in search requests ([34642ee](https://github.com/googleapis/python-retail/commit/34642ee4b9709b56773502d1f6d1c473619c0da1))
* allow users to disable spell check in search requests ([34642ee](https://github.com/googleapis/python-retail/commit/34642ee4b9709b56773502d1f6d1c473619c0da1))


### Bug Fixes

* **deps:** require google-api-core>=1.32.0,>=2.8.0 ([#275](https://github.com/googleapis/python-retail/issues/275)) ([34642ee](https://github.com/googleapis/python-retail/commit/34642ee4b9709b56773502d1f6d1c473619c0da1))
* require python 3.7+ ([#284](https://github.com/googleapis/python-retail/issues/284)) ([7a97063](https://github.com/googleapis/python-retail/commit/7a97063ab2f1093c1a918adb1a78428d687cb9d9))


### Documentation

* deprecate indexable/searchable on the product level custom attributes ([34642ee](https://github.com/googleapis/python-retail/commit/34642ee4b9709b56773502d1f6d1c473619c0da1))
* keep the API doc up-to-date with recent changes ([34642ee](https://github.com/googleapis/python-retail/commit/34642ee4b9709b56773502d1f6d1c473619c0da1))

## [1.6.1](https://github.com/googleapis/python-retail/compare/v1.6.0...v1.6.1) (2022-06-02)


### Bug Fixes

* **deps:** require protobuf <4.0.0dev ([#272](https://github.com/googleapis/python-retail/issues/272)) ([83bb41e](https://github.com/googleapis/python-retail/commit/83bb41e71896338c44d526b6b9028ec7a720c6a3))


### Documentation

* fix changelog header to consistent size ([#273](https://github.com/googleapis/python-retail/issues/273)) ([6a3646f](https://github.com/googleapis/python-retail/commit/6a3646fc43a4bd69d5b7ce2e5982e5a00339637c))

## [1.6.0](https://github.com/googleapis/python-retail/compare/v1.5.0...v1.6.0) (2022-05-19)


### Features

* generate v2alpha/v2beta ([#226](https://github.com/googleapis/python-retail/issues/226)) ([78953f8](https://github.com/googleapis/python-retail/commit/78953f820669aaf9afe592e5c7fc8bed8b5f5e7e))


### Documentation

* fix type in docstring for map fields ([#210](https://github.com/googleapis/python-retail/issues/210)) ([b9f4020](https://github.com/googleapis/python-retail/commit/b9f40205d76962408aa0ae492bd5ed3f5ef07790))
* **samples:** improve the setup scripts ([#207](https://github.com/googleapis/python-retail/issues/207)) ([17dee11](https://github.com/googleapis/python-retail/commit/17dee1119a94392a845cd9855922b6228d25f5d1))

## [1.5.0](https://github.com/googleapis/python-retail/compare/v1.4.1...v1.5.0) (2022-03-30)


### Features

* add new AddLocalInventories and RemoveLocalInventories APIs ([8d61976](https://github.com/googleapis/python-retail/commit/8d619760c771750d55de09fd32deb7e05bf75c8c))
* allow search users to skip validation for invalid boost specs ([8d61976](https://github.com/googleapis/python-retail/commit/8d619760c771750d55de09fd32deb7e05bf75c8c))
* search returns applied control ids in the response ([8d61976](https://github.com/googleapis/python-retail/commit/8d619760c771750d55de09fd32deb7e05bf75c8c))
* support search personalization ([8d61976](https://github.com/googleapis/python-retail/commit/8d619760c771750d55de09fd32deb7e05bf75c8c))
* users cannot switch to empty default branch unless force override ([8d61976](https://github.com/googleapis/python-retail/commit/8d619760c771750d55de09fd32deb7e05bf75c8c))


### Documentation

* deprecate request_id in ImportProductsRequest ([8d61976](https://github.com/googleapis/python-retail/commit/8d619760c771750d55de09fd32deb7e05bf75c8c))
* deprecate search dynamic_facet_spec and suggest to config on cloud console ([8d61976](https://github.com/googleapis/python-retail/commit/8d619760c771750d55de09fd32deb7e05bf75c8c))
* keep the API doc up-to-date with recent changes ([8d61976](https://github.com/googleapis/python-retail/commit/8d619760c771750d55de09fd32deb7e05bf75c8c))
* suggest search users not to send IP and use hashed user id ([8d61976](https://github.com/googleapis/python-retail/commit/8d619760c771750d55de09fd32deb7e05bf75c8c))
* users can self enroll retail search feature on cloud console ([8d61976](https://github.com/googleapis/python-retail/commit/8d619760c771750d55de09fd32deb7e05bf75c8c))

## [1.4.1](https://github.com/googleapis/python-retail/compare/v1.4.0...v1.4.1) (2022-03-05)


### Bug Fixes

* **deps:** require google-api-core>=1.31.5, >=2.3.2 ([#179](https://github.com/googleapis/python-retail/issues/179)) ([398f86d](https://github.com/googleapis/python-retail/commit/398f86d0806f94788e6cb6d4428e4b988ede43f0))
* **deps:** require proto-plus>=1.15.0 ([398f86d](https://github.com/googleapis/python-retail/commit/398f86d0806f94788e6cb6d4428e4b988ede43f0))


### Documentation

* **samples:** fix create bucket for user events ([#173](https://github.com/googleapis/python-retail/issues/173)) ([264f2d4](https://github.com/googleapis/python-retail/commit/264f2d43341ca75284ca30c42e2d9bf6f98195ba))

## [1.4.0](https://github.com/googleapis/python-retail/compare/v1.3.0...v1.4.0) (2022-02-28)


### Features

* add api key support ([#134](https://github.com/googleapis/python-retail/issues/134)) ([234883d](https://github.com/googleapis/python-retail/commit/234883dcd9a02521c76905fc64d79afe6b5782a5))


### Bug Fixes

* resolve DuplicateCredentialArgs error when using credentials_file ([#146](https://github.com/googleapis/python-retail/issues/146)) ([6861dae](https://github.com/googleapis/python-retail/commit/6861dae6d83a8e76950763d83a1926fa5fee465a))


### Documentation

* **samples:** add product import samples ([#149](https://github.com/googleapis/python-retail/issues/149)) ([b4c8608](https://github.com/googleapis/python-retail/commit/b4c860891f2dae7cc4548fe25c4a6b89a36d6987))
* **samples:** add resources for interactive tutorials ([#145](https://github.com/googleapis/python-retail/issues/145)) ([bc60b00](https://github.com/googleapis/python-retail/commit/bc60b00665eee25bf3a6dab701004c0b4171e0dc))
* **samples:** add retail search service samples ([#133](https://github.com/googleapis/python-retail/issues/133)) ([3b5f938](https://github.com/googleapis/python-retail/commit/3b5f9389e19a5ad7b60ea327ebebff3bc561dae7))
* **samples:** add samples for events ([#155](https://github.com/googleapis/python-retail/issues/155)) ([cc475f7](https://github.com/googleapis/python-retail/commit/cc475f7bdfaa5ff8244abca14438d8feea98eacd))
* **samples:** add samples for write/rejoin/purge user events ([#157](https://github.com/googleapis/python-retail/issues/157)) ([4dba447](https://github.com/googleapis/python-retail/commit/4dba4470ebfab01193a4fe39247f121d1af2009e))
* **samples:** add samples to create, read, update, and delete products ([#150](https://github.com/googleapis/python-retail/issues/150)) ([d8f8e34](https://github.com/googleapis/python-retail/commit/d8f8e34885146b0a8386c73a5b820cd5216a4ec7))
* **samples:** Additional guidance in samples/interactive-tutorials/README.md ([#162](https://github.com/googleapis/python-retail/issues/162)) ([47d2388](https://github.com/googleapis/python-retail/commit/47d2388030788022a09302d9556459b4ed62b19e))
* **samples:** read the project id from google.auth ([#160](https://github.com/googleapis/python-retail/issues/160)) ([f6192c8](https://github.com/googleapis/python-retail/commit/f6192c882975565193fc70765e9c97bfd685e5fd))
* **samples:** remove project_number in interactive-tutorials ([#158](https://github.com/googleapis/python-retail/issues/158)) ([017202a](https://github.com/googleapis/python-retail/commit/017202a9e5904fc2e449060791572e6fbd09e60a))

## [1.3.0](https://github.com/googleapis/python-retail/compare/v1.2.1...v1.3.0) (2022-01-14)


### Features

* update grpc service config settings to reflect correct API deadlines ([#120](https://github.com/googleapis/python-retail/issues/120)) ([e7649c7](https://github.com/googleapis/python-retail/commit/e7649c731ed741e7365dc4b9573dcdd770528929))

## [1.2.1](https://www.github.com/googleapis/python-retail/compare/v1.2.0...v1.2.1) (2021-11-01)


### Bug Fixes

* **deps:** drop packaging dependency ([1f05fe4](https://www.github.com/googleapis/python-retail/commit/1f05fe4e88059839627c46f000305f7a2d4c456c))
* **deps:** require google-api-core >= 1.28.0 ([1f05fe4](https://www.github.com/googleapis/python-retail/commit/1f05fe4e88059839627c46f000305f7a2d4c456c))


### Documentation

* fix docstring formatting ([#111](https://www.github.com/googleapis/python-retail/issues/111)) ([fdf5dcd](https://www.github.com/googleapis/python-retail/commit/fdf5dcd5042b9b664186914eea5d4b94fb04eda8))
* list oneofs in docstring ([1f05fe4](https://www.github.com/googleapis/python-retail/commit/1f05fe4e88059839627c46f000305f7a2d4c456c))

## [1.2.0](https://www.github.com/googleapis/python-retail/compare/v1.1.0...v1.2.0) (2021-10-18)


### Features

* add search mode to search request ([#108](https://www.github.com/googleapis/python-retail/issues/108)) ([326576f](https://www.github.com/googleapis/python-retail/commit/326576f696e5890ff240d362e81efba94b835f7e))
* add support for python 3.10 ([#105](https://www.github.com/googleapis/python-retail/issues/105)) ([221e21a](https://www.github.com/googleapis/python-retail/commit/221e21a48a375d7f4b31d6bcf79d77898cb33190))
* update grpc service config settings to reflect correct API deadlines ([326576f](https://www.github.com/googleapis/python-retail/commit/326576f696e5890ff240d362e81efba94b835f7e))


### Documentation

* fix docstring formatting ([#107](https://www.github.com/googleapis/python-retail/issues/107)) ([3777919](https://www.github.com/googleapis/python-retail/commit/37779197eb52c45a347d52a7c3916608d62ec5e1))
* Keep the API doc up-to-date ([326576f](https://www.github.com/googleapis/python-retail/commit/326576f696e5890ff240d362e81efba94b835f7e))

## [1.1.0](https://www.github.com/googleapis/python-retail/compare/v1.0.2...v1.1.0) (2021-10-07)


### Features

* add context manager support in client ([#101](https://www.github.com/googleapis/python-retail/issues/101)) ([3e68d78](https://www.github.com/googleapis/python-retail/commit/3e68d78e6f0c5d2e65f148935446baa92b5dd8ef))

## [1.0.2](https://www.github.com/googleapis/python-retail/compare/v1.0.1...v1.0.2) (2021-09-30)


### Bug Fixes

* improper types in pagers generation ([e82885d](https://www.github.com/googleapis/python-retail/commit/e82885ddcd9926e0b1a5c869e5843c534015b566))

## [1.0.1](https://www.github.com/googleapis/python-retail/compare/v1.0.0...v1.0.1) (2021-09-24)


### Bug Fixes

* add 'dict' annotation type to 'request' ([bee28be](https://www.github.com/googleapis/python-retail/commit/bee28be042f00bc030a789959cb2043b927a6a50))

## [1.0.0](https://www.github.com/googleapis/python-retail/compare/v0.4.2...v1.0.0) (2021-08-25)


### Features

* update grpc service config settings to reflect correct API deadlines ([#82](https://www.github.com/googleapis/python-retail/issues/82)) ([2d535da](https://www.github.com/googleapis/python-retail/commit/2d535dabd51ea101663d45d20b8fe125701a61d3))


### Documentation

* Keep the API doc up-to-date ([#80](https://www.github.com/googleapis/python-retail/issues/80)) ([a77f0ea](https://www.github.com/googleapis/python-retail/commit/a77f0ea03ab1d5a2cb976bb2bff3739c15026558))

## [0.4.2](https://www.github.com/googleapis/python-retail/compare/v0.4.1...v0.4.2) (2021-08-04)


### Documentation

* **retail:** Quote several literal expressions for better rendering ([#75](https://www.github.com/googleapis/python-retail/issues/75)) ([53ede84](https://www.github.com/googleapis/python-retail/commit/53ede84d0115fc3edfb2deab0203ed9fd9dcbf9d))

## [0.4.1](https://www.github.com/googleapis/python-retail/compare/v0.4.0...v0.4.1) (2021-08-01)


### Documentation

* Remove HTML tags from Cloud Retail API library docs ([#73](https://www.github.com/googleapis/python-retail/issues/73)) ([00e0a53](https://www.github.com/googleapis/python-retail/commit/00e0a53b77ba75d2a05c4d72242a6323ed32dfa1))
* remove remaining private links ([#72](https://www.github.com/googleapis/python-retail/issues/72)) ([e2ca897](https://www.github.com/googleapis/python-retail/commit/e2ca897a71fba760d5b838a5fc15307a44024683))

## [0.4.0](https://www.github.com/googleapis/python-retail/compare/v0.3.1...v0.4.0) (2021-07-29)


### Features

* Add restricted Retail Search features for Retail API v2. ([#68](https://www.github.com/googleapis/python-retail/issues/68)) ([84ba173](https://www.github.com/googleapis/python-retail/commit/84ba173d4eadd75cc5289ce76ee800909b20a5ff))

## [0.3.1](https://www.github.com/googleapis/python-retail/compare/v0.3.0...v0.3.1) (2021-07-26)


### Bug Fixes

* **deps:** pin 'google-{api,cloud}-core', 'google-auth' to allow 2.x versions ([#59](https://www.github.com/googleapis/python-retail/issues/59)) ([23223a7](https://www.github.com/googleapis/python-retail/commit/23223a7a195511f4fd63a638f7680999eb4fb554))
* enable self signed jwt for grpc ([#65](https://www.github.com/googleapis/python-retail/issues/65)) ([51b9934](https://www.github.com/googleapis/python-retail/commit/51b9934977c367b4d19a8d104905224386c08c2e))


### Documentation

* add Samples section to CONTRIBUTING.rst ([#60](https://www.github.com/googleapis/python-retail/issues/60)) ([70d0585](https://www.github.com/googleapis/python-retail/commit/70d0585541bb5cfcf698f5223dec3f5a8ebd5b97))


### Miscellaneous Chores

* release 0.3.1 ([#64](https://www.github.com/googleapis/python-retail/issues/64)) ([7ffa868](https://www.github.com/googleapis/python-retail/commit/7ffa868ec872930b37368d9eb7c87ff468b75d48))

## [0.3.0](https://www.github.com/googleapis/python-retail/compare/v0.2.0...v0.3.0) (2021-07-01)


### Features

* add always_use_jwt_access ([#51](https://www.github.com/googleapis/python-retail/issues/51)) ([f6ad4b6](https://www.github.com/googleapis/python-retail/commit/f6ad4b6586924129baecc9fc0536559590518bf6))


### Bug Fixes

* disable always_use_jwt_access ([#55](https://www.github.com/googleapis/python-retail/issues/55)) ([d7f0666](https://www.github.com/googleapis/python-retail/commit/d7f0666dd00706e19bf73656d7379ad01805f61d))


### Documentation

* omit mention of Python 2.7 in 'CONTRIBUTING.rst' ([#1127](https://www.github.com/googleapis/python-retail/issues/1127)) ([#46](https://www.github.com/googleapis/python-retail/issues/46)) ([f03c60a](https://www.github.com/googleapis/python-retail/commit/f03c60ab178f98ceda54d0ed594f83f6af20270f)), closes [#1126](https://www.github.com/googleapis/python-retail/issues/1126)

## [0.2.0](https://www.github.com/googleapis/python-retail/compare/v0.1.0...v0.2.0) (2021-05-28)


### Features

* bump release level to production/stable ([#39](https://www.github.com/googleapis/python-retail/issues/39)) ([c5b1e15](https://www.github.com/googleapis/python-retail/commit/c5b1e15f0d87dc5de7c511cb5b92a396e796ac8b))
* support self-signed JWT flow for service accounts ([879fd90](https://www.github.com/googleapis/python-retail/commit/879fd9014b358f220d47e381f2feac8fc931ea1e))


### Bug Fixes

* add async client to %name_%version/init.py ([879fd90](https://www.github.com/googleapis/python-retail/commit/879fd9014b358f220d47e381f2feac8fc931ea1e))

## 0.1.0 (2021-01-14)


### Features

* generate v2 ([db1013e](https://www.github.com/googleapis/python-retail/commit/db1013e06d8239ce790581f58696e7e9e4aa81a8))
