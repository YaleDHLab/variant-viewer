# Variant Viewer
> Display line-level variants across print/manuscript editions

Variant Viewer is a minimal Jekyll framework for displaying line-level textual variants across multiple editions of a print or manuscript document. Using this framework, scholars can help readers and students understand the ways in which historical documents changed over time.

To use the variant viewer for a project, please consult the quickstart section below.

<table align='center'>
  <tr>
    <td align='center'><img src='assets/images/readme/landing-page.png?raw=true' alt='Landing Page'></td>
    <td align='center'><img src='assets/images/readme/authors-page.png?raw=true' alt='Authors View'></td>
    <td align='center'><img src='assets/images/readme/author-page.png?raw=true' alt='Author View'></td>
    <td align='center'><img src='assets/images/readme/variants-page.png?raw=true' alt='Variants View'></td>
  </tr>
</table>

## Quickstart

To run the variant viewer locally on your machine, you will need to install git and ruby on your machine. Once those are installed, you can run:

```
# clone the source code
git clone https://github.com/YaleDHLab/variant-viewer

# change directories into the source code repository
cd variant-viewer

# install the application dependencies
bundle install

# start the application server
jekyll serve
```

If this all goes well, you should be able to navigate to `localhost:4000/variant-viewer/` in a web browser to see the source code in action.

## Using custom data

The data for this application is defined in JSON files witin the `_data` directory. Please see the Wiki for descriptions of the data schemas of these files.
