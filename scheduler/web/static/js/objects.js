function valueToString(value) {
  if(value < 0) {
    var minus_flag = true;
    value = Math.abs(value);
  } else {
    var minus_flag = false;
  }

  hour = parseInt(value / 3600);
  minute = parseInt((value % 3600) / 60);
  second = value - hour * 3600 - minute * 60

  var time_str = checkTime(hour.toString()) + ":" +  checkTime(minute.toString()) + ":" +  checkTime(second.toString());

  if(minus_flag == true) {
    time_str = "-" + time_str;
  }

  return time_str
};

    var DisplayTime = function(timeString) {
      this.timeStr = timeString;
      var splitted = this.timeStr.split(":");
      this.hour = parseInt(splitted[0]);
      this.minute = parseInt(splitted[1]);
      this.second = parseInt(splitted[2]);

      if(this.hour >= 0){
        this.isNegative = false;
        this.totalSeconds = this.hour * 3600 + this.minute * 60 + this.second;
      } else {
        this.isNegative = true;
        this.totalSeconds = -(Math.abs(this.hour) * 3600 + this.minute * 60 + this.second);
      }
    };

    DisplayTime.prototype.greaterThan = function(displayTime) {
      return (this.totalSeconds > displayTime.totalSeconds);
    };

    DisplayTime.prototype.equal = function(displayTime) {
      return (this.totalSeconds == displayTime.totalSeconds);
    };

    DisplayTime.prototype.valueOf = function() {
      return this.timeStr;
    };

    DisplayTime.prototype.toString = function() {
      return this.timeStr;
    };

    DisplayTime.prototype.minus = function(displayTime) {
      return new DisplayTime(valueToString(this.totalSeconds - displayTime.totalSeconds));
    };

    DisplayTime.prototype.plus = function(displayTime) {
      return new DisplayTime(valueToString(this.totalSeconds + displayTime.totalSeconds));
    };

    var Show = function(data) {
      this.number = data.number;
      this.name = data.name;
      this.duration = new DisplayTime(data.duration);
      this.plan = new DisplayTime(data.plan);
    };

    Show.prototype.toString = function() {
      return {
        'number': this.number,
        'name': this.name,
        'duration': this.duration,
        'plan': this.plan
      }
    }
