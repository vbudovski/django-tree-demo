var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');

module.exports = {
  plugins: [
    new BundleTracker({filename: './dist/webpack-stats.json'})
  ],
  entry: ['./src'],
  output: {
    publicPath: process.env.NODE_ENV == 'development' ? 'http://localhost:3000/' : undefined,
    pathinfo: true,
  },
  devtool: process.env.NODE_ENV == 'development' ? 'eval-source-map' : 'source-map',
  devServer: {
    port: 3000,
    hot: true,
    headers: { "Access-Control-Allow-Origin": "*" }
  },
  resolve: {
    alias: {
      'react-dom': '@hot-loader/react-dom'
    }
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader"
        }
      },
      {
        test: /\.less$/,
        use: [
          {
            loader: 'style-loader', // creates style nodes from JS strings
          },
          {
            loader: 'css-loader', // translates CSS into CommonJS
          },
          {
            loader: 'less-loader', // compiles Less to CSS
            options: {
              javascriptEnabled: true
            }
          },
        ],
      },
    ]
  }
};
