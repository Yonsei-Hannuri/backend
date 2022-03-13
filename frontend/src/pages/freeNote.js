import React, { Component } from 'react';
import axios from 'axios';
import Page from '../components/App/freeNote/page';
import address from '../config/address.json';
import errorReport from '../modules/errorReport';

class FreeNote extends Component {
  static defaultProps = {
    pageSelect: '',
  }

  state = {
    notes: [{}],
    page: 1,
    ajaxError: false,
  };

  componentDidMount() {
    axios({
      method: 'GET',
      url: address.back + 'freeNote/',
      params: { recentNotePage: true },
      withCredentials: true,
    })
      .then((res) => res.data)
      .then((data) => {
        this.setState({ page: data[0].page, notes: data });
      })
      .catch((e) => {
        this.setState({ ajaxError: true });
        errorReport(e, 'FreeNote_componentDidMount');
      });
  }

  getInfoAndPageFlip = (flip) => {
    axios({
      method: 'GET',
      url: address.back + 'freeNote/',
      params: { notePage: this.state.page + flip },
      withCredentials: true,
    })
      .then((res) => res.data)
      .then((data) => {
        this.setState({ page: this.state.page + flip, notes: data });
      })
      .catch((e) => {
        this.setState({ ajaxError: true });
        errorReport(e, 'FreeNote_getInfoAndPageFlip');
      });
  };

  handleUpload = () => {
    this.getInfoAndPageFlip(0);
  };

  handleNextPage = () => {
    if (this.state.page + 1 < 101) {
      this.getInfoAndPageFlip(1);
    }
  };
  handlePreviousPage = () => {
    if (this.state.page - 1 > 0) {
      this.getInfoAndPageFlip(-1);
    }
  };

  render() {
    return (
      <div>
        <button
          className="btn col-3 border mx-1 btn-light"
          onClick={this.handlePreviousPage}
        >
          이전
        </button>
        <button
          className="btn col-3 border mx-1 btn-light"
          onClick={this.handleNextPage}
        >
          다음
        </button>
        <span className="col-3 mx-1">페이지 {this.state.page}</span>
        {this.state.ajaxError ? (
          <span className="text-danger">
            페이지 불러오는 중 오류가 발생했습니다.
          </span>
        ) : (
          ''
        )}
        <button onClick={this.props.pageSelect} name='metaSpace' className="btn col-3 border float-end mx-1 btn-light">
          나가기
        </button>
        <Page
          info={this.state.notes}
          onUpload={this.handleUpload}
          page={this.state.page}
        />
      </div>
    );
  }
}

export default FreeNote;
