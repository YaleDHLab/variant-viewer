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

## Seeding development data

To seed data for tweaking layouts, you can run:
```
python utils/seed_data.py && python utils/write_pages.py
```

## Using custom data

The data expressed by this application is defined in YAML files witin the `_data` directory. These files are generated from user-provided files specified in `utils/data/data-manifest.yaml`.

#### DATA MANIFEST

To renegerate the site using custom data, one must first update the `data-manifest`, using the following format:

```
authors:                                # LIST OF AUTHORS
  - author_id:                          UNIQUE IDENTIFIER FOR AUTHOR
    author_bio:                         SHORT AUTHOR BIO
    author_name:                        AUTHOR'S NAME
    author_image:                       PATH TO AUTHOR IMAGE

    author_works:                       # LIST OF WORKS BY `AUTHOR`
      - work_id:                        UNIQUE IDENTIFIER FOR WORK
        work_name:                      NAME OF WORK
        work_image:                     IMAGE OF WORK
        work_introduction:              SHORT INTRODUCTION TO WORK

        print:                          # DATA ON A PRINT PUBLICATION OF `WORK`
          print_title:                  TITLE OF PRINT PUBLICATION
          print_images:                 LIST OF IMAGES IN PRINT PUBLICATION

        genetic:                        # DATA ON GENETIC OVERVIEW OF WORK
          genetic_data:                 PATH TO GENETIC YAML DATA

        work_witnesses:                 # CONTAINS DATA ON WITNESSES OF THE WORK
          - witness_name:               UNIQUE NAME FOR WITNESS
            witness_xml:                PATH TO WITNESS XML
            witness_image_directory:    DIRECTORY WITH WITNESS IMAGES
            witness_image_extension:    FILE EXTENSION OF WITNESS IMAGES
```



Example:
```
authors:
  - author_name: Ezra Pound
    author_id: pound
    author_image: /utils/data/authors/pound/ezra-pound.jpg
    author_bio: >
      The importance of Pound's contributions to the arts and to the revitalization of poetry early in this century has been widely acknowledged; yet in 1950, Hugh Kenner could claim in his groundbreaking study The Poetry of Ezra Pound, "There is no great contemporary writer who is less read than Ezra Pound." Pound never sought, nor had, a wide reading audience; his technical innovations and use of unconventional poetic materials often baffled even sympathetic readers. Early in his career, Pound aroused controversy because of his aesthetic views; later, because of his political views. For the greater part of this century, however, Pound devoted his energies to advancing the art of poetry and maintaining his aesthetic standards in the midst of extreme adversity.
    author_works:
      - work_name: Canto 6
        work_id: canto-6
        work_image: /utils/data/authors/pound/works/canto-6/ezra-pound-canto-6.jpg
        work_introduction: >
          Ezra Pound referred to Canto 6 as, variously, ‘an epic including history’ and, with more muted self-praise, a ‘ragbag’. Yet although it is undeniably a ragbag, there are a number of key themes running through The Cantos. Pound has started out with Imagism, in 1912, and the idea of ‘superposition’: placing, as it were, one image on top of another, so that in his most famous early poem, the two-line ‘In a Station of the Metro’, the faces of the commuters in the Metro station are placed next to the image of petals on the wet, black bough of a tree. In a sense, The Cantos sets out to apply such a principle, not to individual images, but to whole epochs and systems: capitalism, history, politics, economics, art, poetry, and the relation between these various disciplines and institutions. For instance, art and finance are connected through a theme that is glimpsed at several points in The Cantos, namely the relationship between an artist and his patron.
        print:
          print_title: Three Mountains Edition (1925)
          print_images:
            - /utils/data/authors/pound/works/canto-6/print/images/10504119.jpg
            - /utils/data/authors/pound/works/canto-6/print/images/10504120.jpg
            - /utils/data/authors/pound/works/canto-6/print/images/10504121.jpg
        genetic:
          genetic_data: utils/data/authors/pound/works/canto-6/genetic/canto-6-genetic.yaml
        work_witnesses:
          - witness_name: 'Witness 3130'
            witness_image_directory: /utils/data/authors/pound/works/canto-6/diplomatic/canto-6-witness-3130/images/
            witness_image_extension: '.jpg'
            witness_xml: utils/data/authors/pound/works/canto-6/diplomatic/canto-6-witness-3130/xml/canto-6-witness-3130.xml
```