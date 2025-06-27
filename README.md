<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<h3 align="center">.dat to .txt Extractor</h3>

  <p align="center">
    <a href="https://github.com/mattsteen14/dat_txt_extractor"><strong>Explore the docs »</strong></a>
    <br />
    <br />
     <a href="https://github.com/mattsteen14/dat_txt_extractor">View Demo</a>
    ·
    <a href="https://github.com/mattsteen14/dat_txt_extractor/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/mattsteen14/dat_txt_extractor/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

This Python script extracts game descriptions from Skraper generated .dat files (XML format) and saves each description as a separate .txt file. Each output file is named after the ROM (e.g. Super Metroid (Japan, USA) (En,Ja).zip → Super Metroid (Japan, USA) (En,Ja).txt) and contains only the game’s text description.

Ideal for use with Skraper metadata exports and retro gaming setups like MUOS or Anbernic handhelds.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

- Python

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

These are instructions for setting up the project locally. To get a local copy up and running, follow these simple steps.

### Prerequisites

Ensure you have the following software installed before proceeding:

- **Python 3.6 or higher installed**: Check with:

  ```sh
  python3 --version
  ```

### Installation

<!-- 1. Get a free API Key at [https://example.com](https://example.com) -->
1. Clone the repository:

   ```sh
   git clone https://github.com/mattsteen14/dat_txt_extractor.git
   ```

2. Navigate into the project directory:

   ```sh
   cd dat_txt_extractor
   ```

3. Run the script from the terminal using:

   ```sh
   python3 datxt.py --dat "/path/to/your/file.dat" --output "/path/to/output_folder"
   ```

    *Hint:* 
    
    *Instead of typing the full paths, just drag & drop the file & the folder into the terminal.*

4. Running the script will:

- Read the Skraper .dat file
- Extract the description for each < game >
- Save it to a .txt file named after the < rom name > (minus the extension)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

- [x] Plan project.
- [x] Write code.
- [x] Test on .dat files.
- [x] Version control. Set up on GitHub.
- [x] Push to GitHub.
- [ ] Testing and dubugging.
- [ ] Additional features.
- [ ] Create simple GUI interface.

See the [open issues](https://github.com/mattsteen14/dat_txt_extractor/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project.

2. Create your Feature Branch:

   ```sh
   git checkout -b feature/AmazingFeature
   ```

3. Commit your Changes:

   ```sh
   git commit -m "Add some AmazingFeature"
   ```

4. Push to the Branch:

   ```sh
   git push origin feature/AmazingFeature
   ```

5. Open a Pull Request.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Matt Steen-Brookes - [@mattsteen14](https://twitter.com/mattsteen14) - <mattsteen14@me.com>

Project Link: [https://github.com/mattsteen14/dat_txt_extractor](https://github.com/mattsteen14/dat_txt_extractor)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

- [Mo Ashqar](https://github.com/ashqar) for introducing me to Codecademy in the first place.
- [Othneil Drew](https://github.com/othneildrew) for the README template.
- [Choose an Open Source License](https://choosealicense.com)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/mattsteen14/dat_txt_extractor.svg?style=for-the-badge
[contributors-url]: https://github.com/mattsteen14/dat_txt_extractor/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/mattsteen14/dat_txt_extractor.svg?style=for-the-badge
[forks-url]: https://github.com/mattsteen14/dat_txt_extractor/network/members
[stars-shield]: https://img.shields.io/github/stars/mattsteen14/dat_txt_extractor.svg?style=for-the-badge
[stars-url]: https://github.com/mattsteen14/dat_txt_extractor/stargazers
[issues-shield]: https://img.shields.io/github/issues/mattsteen14/dat_txt_extractor.svg?style=for-the-badge
[issues-url]: https://github.com/mattsteen14/dat_txt_extractor/issues
[license-shield]: https://img.shields.io/github/license/mattsteen14/dat_txt_extractor.svg?style=for-the-badge
[license-url]: https://github.com/mattsteen14/dat_txt_extractor/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/mattsteen14
