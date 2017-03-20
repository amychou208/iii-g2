'use strict';

var _class, _temp;

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var App = (_temp = _class = function (_React$Component) {
	_inherits(App, _React$Component);

	function App(props) {
		_classCallCheck(this, App);

		var _this = _possibleConstructorReturn(this, _React$Component.call(this, props));

		_this.state = {
			leaderboard: [],
			lastMonthLeaders: [],
			allTimeLeaders: []
		};
		_this.switchToAllTimeLeaders = _this.switchToAllTimeLeaders.bind(_this);
		_this.switchToLastMonthLeaders = _this.switchToLastMonthLeaders.bind(_this);
		return _this;
	}

	App.prototype.switchToAllTimeLeaders = function switchToAllTimeLeaders() {
		this.setState({
			leaderboard: this.state.allTimeLeaders
		});
	};

	App.prototype.switchToLastMonthLeaders = function switchToLastMonthLeaders() {
		this.setState({
			leaderboard: this.state.lastMonthLeaders
		});
	};

	App.prototype.getCampers = function getCampers(url) {
		this.serverRequest = $.getJSON(url, function (data) {
			if (url === this.props.pastMonthLeaders) {
				this.setState({
					lastMonthLeaders: data,
					leaderboard: data
				});
			} else {
				this.setState({
					allTimeLeaders: data
				});
			}
		}.bind(this), 'jsonp');
	};

	App.prototype.componentDidMount = function componentDidMount() {
		this.getCampers(this.props.pastMonthLeaders);
		this.getCampers(this.props.allTimeLeaders);
	};

	App.prototype.render = function render() {

		return React.createElement(TableComponent, { leaderboard: this.state.leaderboard, switchToAllTimeLeaders: this.switchToAllTimeLeaders, switchToLastMonthLeaders: this.switchToLastMonthLeaders });
	};

	return App;
}(React.Component), _class.defaultProps = {
	pastMonthLeaders: '../../media/recent.txt',
	allTimeLeaders: '../../media/alltime.txt'
}, _temp);

var TableComponent = function (_React$Component2) {
	_inherits(TableComponent, _React$Component2);

	function TableComponent() {
		_classCallCheck(this, TableComponent);

		return _possibleConstructorReturn(this, _React$Component2.apply(this, arguments));
	}

	TableComponent.prototype.render = function render() {
		console.log(this.props);
		if (!this.props.leaderboard) {
			return React.createElement(
				'div',
				{ className: 'noLeaderBoard' },
				'No Leaderboard'
			);
		}
		var count=0;//me
		var idx = 0,
		    campers = this.props.leaderboard.map(function (camper, idx) {
				
		count=idx; //me
		if(idx<10){ //me
			return React.createElement(RowComponent, { key: camper.username, camper: camper, id: idx + 1 });
			};//me
		});

		return React.createElement(
			'div',
			{ className: 'table-responsive' },
			React.createElement(
				'table',
				{ className: 'table table-striped table-bordered' },
				React.createElement(
					'caption',
					{ className: 'no_pad' },
					React.createElement(
						'div',
						{ className: 'table_title' },
						'我的明星臉'
					)
				),
				React.createElement(
					'thead',
					null,
					React.createElement(
						'tr',
						null,
						React.createElement(
							'th',
							null,
							'#'
						),
						React.createElement(
							'th',
							null,
							'Celibrity name'
						),
						// React.createElement(
							// 'th',
							// { className: 'trigger', onClick: this.props.switchToLastMonthLeaders },
							// '相似度'
						// ),
						React.createElement(
							'th',
							{ className: 'trigger', onClick: this.props.switchToAllTimeLeaders },
							'相似度'
						)
					)
				),
				React.createElement(
					'tbody',
					null,
					campers
				)
			)
		);
	};

	return TableComponent;
}(React.Component);

var RowComponent = function (_React$Component3) {
	_inherits(RowComponent, _React$Component3);
	
	function RowComponent() {
		_classCallCheck(this, RowComponent);
		
		return _possibleConstructorReturn(this, _React$Component3.apply(this, arguments));
	}
	
	
	RowComponent.prototype.render = function render() {
		
	console.log(this.props);
		return React.createElement(
			'tr',
			null,
			React.createElement(
				'td',
				null,
				this.props.id
			),
			React.createElement(
				'td',
				null,
				React.createElement('img', { className: 'img-responsive', src: this.props.camper.img }),
				this.props.camper.username
			),
			// React.createElement(
				// 'td',
				// { className: 'text-center' },
				// this.props.camper.recent
			// ),
			React.createElement(
				'td',
				{ className: 'text-center' },
				this.props.camper.alltime
			)
		);
	};

	return RowComponent;
}(React.Component);

ReactDOM.render(React.createElement(App, null), document.body);