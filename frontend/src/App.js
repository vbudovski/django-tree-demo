import React from 'react';
import { Tree, Typography, Layout } from 'antd';

import 'antd/dist/antd.less';

const { Header, Content } = Layout;
const { Title } = Typography;


class App extends React.Component {
  state = {
    treeData: null
  };

  processNodes(nodes) {
    return nodes.map(({ node, children }) => ({
      key: node.pk,
      title: node.name,
      children: this.processNodes(children),
    }));
  }

  loadData = () => {
    return fetch('/api/categories/').then(
      (response) => {
        response.json().then(
          (data) => {
            this.setState({ treeData: this.processNodes(data) });
          },
        );
      },
    );
  };

  handleMove = (node, dragNode, before) => {
    const endpoint = before ? 'move-before' : 'move-after';

    return fetch(
      `/api/categories/${dragNode.key}/${endpoint}/`,
      {
        method: 'post',
        body: JSON.stringify({ node: node.key }),
        headers: {
          'Content-Type': 'application/json',
        },
      },
    )
  };

  handleDrop = async ({ event, node, dragNode }) => {
    if (node.dragOverGapTop) {
      await this.handleMove(node, dragNode, true);
    } else if (node.dragOverGapBottom) {
      await this.handleMove(node, dragNode, false);
    }
    this.loadData();
  };

  componentDidMount() {
    this.loadData();
  }

  render() {
    const { treeData } = this.state;

    return (
      <Layout>
        <Content>
          <Title>Categories</Title>

          <Tree
            treeData={treeData}
            draggable
            onDrop={this.handleDrop}
          />
        </Content>
      </Layout>
    );
  }
}

export default App;
