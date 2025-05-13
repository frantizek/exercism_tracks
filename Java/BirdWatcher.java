
class BirdWatcher {
    private final int[] birdsPerDay;

    public BirdWatcher(int[] birdsPerDay) {
        this.birdsPerDay = birdsPerDay.clone();
    }

    public int[] getLastWeek() {
        return birdsPerDay;
    }

    public int getToday() {
        return birdsPerDay[6];
    }

    public void incrementTodaysCount() {
        this.birdsPerDay[6] = birdsPerDay[6]+1; 
    }

    public boolean hasDayWithoutBirds() {
        for(int day: birdsPerDay) {
            if (day == 0) {
                return true;
            }            
        }
        return false;
    }

    public int getCountForFirstDays(int numberOfDays) {
        if (numberOfDays >= 7){
            numberOfDays = 7;
        }
        int numberOfBirds = 0;
        for (int i = 0; i < numberOfDays; i++) {
            numberOfBirds +=  birdsPerDay[i];
        }
        return numberOfBirds;
    }

    public int getBusyDays() {
        int busyDays = 0;
        for(int day: birdsPerDay) {
            if (day >= 5) {
                busyDays += 1;
            }
        }
        return busyDays;
    }
}
