const makeConfig = require('idgx-recipe-staticresources');
const CopyWebpackPlugin = require('copy-webpack-plugin');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const SpritesmithPlugin = require('webpack-spritesmith');

let createTheme = (theme) => {
  let publicPath = `++theme++${theme}/`;

  return makeConfig(
    // name
    'idgx.temas',

    //shortName
    'idgxtemas',

    //path
    `${__dirname}/../src/idgx/temas/themes/${theme}`,

    //publicPath
    publicPath,

    // callback
    function(config, options) {
      config.entry.unshift(
        `./app/${theme}/preview.png`,
        `./app/${theme}/idgxtemas.less`,
      );
      // Change image handler context
      config.module.rules[2].use[0].options.context = `app/${theme}/`;
      config.plugins.push(
        new CopyWebpackPlugin([
          { from: 'app/rules.xml', to: 'rules.xml' },
          { from: `app/${theme}/manifest.cfg`, to: 'manifest.cfg' },
          { from: `app/img`, to: 'img' },
        ], {
        }),
      );
    },
  );
};


module.exports = [
  createTheme('padrao'),
  createTheme('padrao-verde'),
  createTheme('padrao-amarelo'),
  createTheme('cor-azul'),
  createTheme('cor-verde'),
  createTheme('cor-amarelo'),
];
