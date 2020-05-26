# EASYDB-PICKER

Search for objects in heidICON via the text, title and shot-ID. This
script sends requirements to the heidICON server for reaching the
collection of all objects in the public pools. First the user has to
type a search value and then after the 'PICK' button is pressed, will
begin the search. On the screen will appear a dynamic form of found
objects, where the user can select one and include the results and the
asset-deep-link inside a targetsystem.

## Getting Started

After you get a copy of this project, you can find the `demo` folder
and running the `index.html` on your local machine. All public values
that you can find without login at
[https://heidicon.ub.uni-heidelberg.de](https://heidicon.ub.uni-heidelberg.de)
are available. For example start with values `Phaeton`, phrases `"The
Fall of Phaeton"` or both `Fall "Fall of Phaeton" of Phaeton` .

## Requirements

There is no special installation requirement.

## Configurations

Please configure global JSON `window.easydbpickerconfig` superset
features for the right search request.  An array of pools restricts
the search to specific pools in heidICON.  The next collection
represents the different type of search e.g. `title` or `fulltext` are
distingt from each other and needs different settings in the post.
`Title` search has to set the `bool` option to `must`and means logical
`and` during `should` means logical `or` and give more available
results. You can continue this list with other terms as `fulltext` but
with the same options as follows `de` and more languages, `bool`,
`objecttype` and `fields`.


## Deployment

The main skript `easydbpicker.js` has some dependencies. If you start
the searching process, you'll probably use a `picker button` and an
`input field` for typing the search value in heidICON. In Addition pick
the right result information of the selected heidICON object, that
will appear in configurated fields of the targetsystem. The decisive
method is called `start`, that expects three parameters. Namely the
`search value` of the input field, the `dom element`, where to apply
the dynamic form of results and the `callback function`, that decide
how to include the results, what to do with the result values or where
to write whem.

## Contributing

Please read [CONTRIBUTING.md](/CONTRIBUTING.md) for details on our
code of conduct, and the process for submitting pull requests to us.

## Author

```
Universitätsbibliothek Heidelberg
Jelena Ekimotcheva
- Informationstechnologie -
Email: Ekimotcheva@ub.uni-heidelberg.de
```

## License

This project is licensed under the MIT License - see the
[LICENSE.md](/LICENSE.md) file for details.


